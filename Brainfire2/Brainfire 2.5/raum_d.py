import random
import pprint
import time
from copy import deepcopy

class VEC:

    def __init__(self, z, y, x):
        self.z = int(z)
        self.y = int(y)
        self.x = int(x)


    def __eq__(self, other):
        return self.z == other.z and self.y == other.y and self.x == other.x


    def __add__(self, other):
        return VEC(self.z + other.z, self.y + other.y, self.x + other.x)


    def __sub__(self, other):
        return VEC(self.z - other.z, self.y - other.y, self.x - other.x)


    def __hash__(self):
        return hash(str(self))


    def invert(self):
        return VEC(self.z, -self.y, -self.x)


    def inText(self, bz=True):
        text = ""
        if bz:
            text += str(self.z)
        text += " " + str(self.y) + " " + str(self.x)
        return text


class ROOM_NODE:

    def __init__(self, pos):
        self.position = VEC(pos.z, pos.y, pos.x)
        self.reachable_doors = set()
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
        self.reachable_doors.add(door)
        for pre in self.predecessors:
            pre.add_door(door)


class ROOM:

    def __init__(self, ID, stone_treshold=0.2, portal_treshold=0.5):
        self.ID = ID
        self.sy = roomsize_y
        self.sx = roomsize_x
        self.matrix = [[[None for x in range(self.sx)] for y in range(self.sy)] for z in range(layers)]
        self.init_matrix(stone_treshold, portal_treshold)

        self.connections = [[False for x in range(len(doors))] for y in range(len(doors))]

        self.reachable_points = set()


    def init_matrix(self, s_treshold, p_treshold):
        for z in range(layers):
            for y in range(self.sy):
                for x in range(self.sx):
                    if random.random() < s_treshold:
                        self.matrix[z][y][x] = 1
                    else:
                        self.matrix[z][y][x] = 0

        if settings["portals"] and layers == 2:
            if random.random() > p_treshold:
                y = random.randint(1, self.sy - 2)
                x = random.randint(1, self.sx - 2)
                self.matrix[0][y][x] = 2
                self.matrix[1][y][x] = 2
                for vec in doors.keys():
                    self.matrix[vec.z][y + vec.y][x + vec.x] = 0

        for door in doors.values():
            self.matrix[door.z][door.y][door.x] = 0


    def print_matrix(self):
        for z in range(layers):
            if z:
                print("Underworld:")
            else:
                print("Overworld:")
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
                    line += str(self.matrix[z][y][x]) + "  "
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

        if value == 2:
            new.z = int(not new.z)
            return self.run(new, vec)


    def inBound(self, pos):
        return (pos.z == 0 or pos.z == 1) and (pos.y >= 0 and pos.y < self.sy) and (pos.x >= 0 and pos.x < self.sx)


    def get_from_vec(self, vec):
        return self.matrix[vec.z][vec.y][vec.x]




class ROOM_SOLVER:

    def __init__(self, room):
        self.room = room

        self.nodes = [[[None for x in range(roomsize_x)] for y in range(roomsize_y)] for z in range(layers)]

    def get_node(self, vec):
        value = self.nodes[vec.z][vec.y][vec.x]
        if value == None:
            value = ROOM_NODE(vec)
            self.nodes[vec.z][vec.y][vec.x] = value

        return value


    def solve(self):

        visited = []
        door_nodes = [self.get_node(door_pos) for door_pos in doors.values()]
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
                    diff.z = node.position.z
                    if diff.y != 0:
                        diff.y /= abs(diff.y)
                    if diff.x != 0:
                        diff.x /= abs(diff.x)

                for direction in directions:
                    if direction != diff and direction.invert() != diff:
                        queue.append(self.get_node(self.room.run(node.position, direction)))



def debug(text):
    if settings["debug"]:
        print(text)


settings = {
    "portals" : True,
    "debug" : True
}

roomsize_y = 16
roomsize_x = 16
layers = int(settings["portals"]) + 1

cid = 1


if layers == 1:
    doors = {
        VEC(0, -1, 0): VEC(0, 0, roomsize_x / 2 - 1),
        VEC(0, 0, -1): VEC(0, roomsize_y / 2, 0),
        VEC(0, 1, 0): VEC(0, roomsize_y - 1, roomsize_x / 2),
        VEC(0, 0, 1): VEC(0, roomsize_y / 2 - 1, roomsize_x - 1)
    }
else:
    doors = {
        VEC(0, -1, 0): VEC(0, 0, roomsize_x / 2 - 1),
        VEC(0, 0, -1): VEC(0, roomsize_y / 2, 0),
        VEC(0, 1, 0): VEC(0, roomsize_y - 1, roomsize_x / 2),
        VEC(0, 0, 1): VEC(0, roomsize_y / 2 - 1, roomsize_x - 1),
        VEC(1, -1, 0): VEC(1, 0, roomsize_x / 2 - 1),
        VEC(1, 0, -1): VEC(1, roomsize_y / 2, 0),
        VEC(1, 1, 0): VEC(1, roomsize_y - 1, roomsize_x / 2),
        VEC(1, 0, 1): VEC(1, roomsize_y / 2 - 1, roomsize_x - 1)
    }

directions = [
    VEC(0, -1, 0),
    VEC(0, 0, -1),
    VEC(0, 1, 0),
    VEC(0, 0, 1)
]


def create_room(id):
    r = ROOM(id)
    s = ROOM_SOLVER(r)
    s.solve()
    return r


def mass_production_single(ammount):
    rooms = []
    for id in range(cid, cid+ammount):
        rooms.append(create_room(id))
    id += ammount
    return rooms


if __name__ == '__main__':
    time.clock()
    random.seed(1)

    mass_production_single(1000)

    print(time.clock())
