import random
import pprint
import time
from copy import deepcopy
import multiprocessing

class VEC:

    def __init__(self, y, x):
        self.y = int(y)
        self.x = int(x)


    def __eq__(self, other):
        return self.y == other.y and self.x == other.x


    def __add__(self, other):
        return VEC(self.y + other.y, self.x + other.x)


    def __sub__(self, other):
        return VEC(self.y - other.y, self.x - other.x)


    def __hash__(self):
        return hash(str(self.y) + str(self.x))


    def invert(self):
        return VEC(-self.y, -self.x)


    def inText(self):
        text = ""
        text += " " + str(self.y) + " " + str(self.x)
        return text


class ROOM_NODE:

    def __init__(self, pos):
        self.position = VEC(pos.y, pos.x)
        self.reachable_doors = []
        self.predecessors = []

    def __eq__(self, other):
        if other == None:
            return False
        return self.position == other.position


    def add_predecessor(self, node):
        if node == None:
            return
        if node == self:
            return
        if node in self.predecessors:
            return
        self.predecessors.append(node)


    def add_door(self, door):
        if door not in self.reachable_doors:
            self.reachable_doors.append(door)
            for pre in self.predecessors:
                pre.add_door(door)


    def terminate(self):
        while self.reachable_doors:
            del(self.reachable_doors[0])
        while self.predecessors:
            del(self.predecessors[0])
        del(self.position)



class ROOM:

    def __init__(self, ID, stone_treshold=0.2):
        self.ID = ID
        self.sy = roomsize_y
        self.sx = roomsize_x
        self.matrix = [[None for x in range(self.sx)] for y in range(self.sy)]
        self.init_matrix(stone_treshold)

        self.connections = [[False for x in range(len(doors))] for y in range(len(doors))]

        self.reachable_points = set()


    def init_matrix(self, s_treshold):
        for y in range(self.sy):
            for x in range(self.sx):
                if random.random() < s_treshold:
                    self.matrix[y][x] = 1
                else:
                    self.matrix[y][x] = 0

        for door in doors.values():
            self.matrix[door.y][door.x] = 0


    def print_matrix(self):
        line = "     "
        for y in range(self.sy):
            if y >= 10:
                line += "1  "
            else:
                line += "   "
        print(line)
        line = "     "
        for y in range(self.sy):
            line += str(y % 10) + "  "
        print(line)
        print()
        for y in range(self.sy):
            line = ""
            if y <= 9:
                line += " "
            line += str(y) + "   "
            for x in range(self.sx):
                line += str(self.matrix[y][x]) + "  "
            print(line)
        print()


    def run(self, start, vec):
        new = start + vec

        if not self.inBound(new):
            return start

        value = self.get_from_vec(new)

        if value == 0:
            return self.run(new, vec)

        if value == 1:
            return start


    def inBound(self, pos):
        return (pos.y >= 0 and pos.y < self.sy) and (pos.x >= 0 and pos.x < self.sx)


    def get_from_vec(self, vec):
        return self.matrix[vec.y][vec.x]


class ROOM_SOLVER:

    def __init__(self, room):
        self.room = room

        self.nodes = [[None for x in range(roomsize_x)] for y in range(roomsize_y)]

    def get_node(self, vec):
        value = self.nodes[vec.y][vec.x]
        if value == None:
            value = ROOM_NODE(vec)
            self.nodes[vec.y][vec.x] = value

        return value


    def solve(self):

        visited = []
        door_nodes = [self.get_node(door_pos) for door_pos in doors.values()]
        debug(door_nodes)
        for door in door_nodes:
            queue = [door]
            last = None
            while queue:
                node = queue.pop(0)
                node.add_predecessor(last)
                last = node
                if node in visited:
                    continue
                visited.append(node)
                diff = None
                if last != None:
                    diff = node.position - last.position
                    if diff.y != 0:
                        diff.y /= abs(diff.y)
                    if diff.x != 0:
                        diff.x /= abs(diff.x)

                for direction in directions:
                    if direction != diff and direction.invert() != diff:
                        queue.append(self.get_node(self.room.run(node.position, direction)))

        for door in door_nodes:
            door.add_door(door.position)

        door_list = list(doors.values())
        for door in door_nodes:
            for reach in door.reachable_doors:
                self.room.connections[door_list.index(door.position)][door_list.index(reach)] = True

        for row in self.nodes:
            for node in row:
                if node:
                    node.terminate()
                    del(node)

        while visited:
            del(visited[0])


def debug(text):
    if settings["debug"]:
        print(text)


settings = {
    "portals" : True,
    "debug" : True
}

roomsize_y = 16
roomsize_x = 16

cid = 1

if settings["portals"]:
    doors = {
        VEC(-1, 0): VEC(0, roomsize_x / 2 - 1),
        VEC(0, -1): VEC(roomsize_y / 2, 0),
        VEC(1, 0): VEC(roomsize_y - 1, roomsize_x / 2),
        VEC(0, 1): VEC(roomsize_y / 2 - 1, roomsize_x - 1),
        VEC(0, 0): VEC(roomsize_y / 2, roomsize_x / 2)
    }
else:
    doors = {
        VEC(-1, 0): VEC(0, roomsize_x / 2 - 1),
        VEC(0, -1): VEC(roomsize_y / 2, 0),
        VEC(1, 0): VEC(roomsize_y - 1, roomsize_x / 2),
        VEC(0, 1): VEC(roomsize_y / 2 - 1, roomsize_x - 1)
    }

directions = [
    VEC(-1, 0),
    VEC(0, -1),
    VEC(1, 0),
    VEC(0, 1)
]


def create_room(id):
    r = ROOM(id)
    s = ROOM_SOLVER(r)
    s.solve()
    return r


def mass_production_single(ammount):
    rooms = []
    for id in range(cid, cid + ammount):
        rooms.append(create_room(id))
    cid += ammount
    return rooms


def mass_production_multi(ammount):
    rooms = []
    for id in range(cid, cid + ammount):
        rooms.append(ROOM(id))
    print("Starting multiprocessing on", multiprocessing.cpu_count(), "cores...")
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    pool.map(room_creation_process, rooms)
    print("Done")
    return rooms


def room_creation_process(room):
    solver = ROOM_SOLVER(room)
    solver.solve()



if __name__ == '__main__':
    r = create_room(-1)
    r.print_matrix()
    pprint.pprint(r.connections)

    exit()
    time.clock()
    random.seed(1)

    rooms = mass_production_multi(1000)

    print(time.clock())

    pprint.pprint(rooms[0].connections)

