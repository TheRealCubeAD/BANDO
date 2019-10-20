import raum
import time
import random
import copy
import pprint

POS = raum.POS

class template:

    def __init__(self,ny,nx):
        self.y = ny
        self.x = nx
        self.infected = False

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x




class LEVEL:

    def __init__(self,nsy=6,nsx=6):
        self.sy = nsy
        self.sx = nsx
        self.matrix = [[None for _ in range(self.sx)] for __ in range(self.sy)]
        self.startPos = POS(0,0)
        self.endPos = POS(random.randint(int(nsy/2),nsy),random.randint(int(nsx/2),nsx))
        self.pathLenght = None


class LEVEL_SOLVER:

    def __init__(self,nLevel):
        self.level = nLevel
        self.tpl_mtx = []
        for y in range(self.level.sy):
            row = []
            for x in range(self.level.sx):
                row.append(template(y,x))
            self.tpl_mtx.append(row)

        self.storage = [[],[],[],[]]
        self.path = None



    def solve(self):
        not_infected = []
        for row in self.tpl_mtx:
            not_infected += row
        not_infected.remove(self.tpl_mtx[self.level.startPos.y][self.level.startPos.x])
        self.tpl_mtx[self.level.startPos.y][self.level.startPos.x].infected = True
        self.level.matrix[self.level.startPos.y][self.level.startPos.x] = raum.createRoom(0)

        snake = []
        snake += self.get_neighbours(self.tpl_mtx[self.level.startPos.y][self.level.startPos.x],snake)

        while snake:
            R = random.choice(snake)
            snake.remove(R)
            P = self.get_rand_inf_neighbour(R)
            diff = POS(P.y-R.y,P.x-R.x)
            self.place_room(R,diff)
            R.infected = True
            not_infected.remove(R)
            snake += self.get_neighbours(R,snake)



    def get_neighbours(self,tpl,snake):
        neigh = [POS(tpl.y + 1, tpl.x), POS(tpl.y - 1, tpl.x), POS(tpl.y, tpl.x + 1), POS(tpl.y, tpl.x - 1)]
        res = []

        for t in neigh:
            if t.y not in range(self.level.sy) or t.x not in range(self.level.sx):
                pass
            else:
                item = self.tpl_mtx[t.y][t.x]
                if item not in snake and not item.infected:
                    res.append(self.tpl_mtx[t.y][t.x])

        return res


    def get_rand_inf_neighbour(self, tpl):
        neigh = [POS(tpl.y+1,tpl.x),POS(tpl.y-1,tpl.x),POS(tpl.y,tpl.x+1),POS(tpl.y,tpl.x-1)]
        res = []

        for t in neigh:
            if t.y not in range(self.level.sy) or t.x not in range(self.level.sx):
                pass
            elif not self.tpl_mtx[t.y][t.x].infected:
                pass
            else:
                res.append(self.tpl_mtx[t.y][t.x])

        return random.choice(res)



    def place_room(self,tpl,dir):
        dir_index = dirs.index(dir)
        while not self.storage[dir_index]:
            self.call_rooms()
        room = self.storage[dir_index][0]
        del(self.storage[dir_index][0])
        self.level.matrix[tpl.y][tpl.x] = room


    def check_room(self,room,dir_index):
        for row in room.connections:
            if not row[dir_index]:
                return False

        return True

    def call_rooms(self):
        rooms = raum.massProduction(100)
        for room in rooms:
            for i in range(4):
                if self.check_room(room,i):
                    self.storage[i].append(room)
                    break


    def determine_path(self):
        return self.make_path([],self.level.startPos)


    def make_path(self,path,pos):
        if pos.y not in range(self.level.sy) or pos.x not in range(self.level.sx):
            return None
        if pos in path:
            return None

        path.append(pos)
        if pos == self.level.endPos:
            return path

        if len(path) > int((self.level.sy + self.level.sx)*1.5):
            return None


        cur_dirs = copy.deepcopy(dirs)
        random.shuffle(cur_dirs)

        for dir in cur_dirs:
            res = self.make_path(copy.deepcopy(path),pos + dir)
            if res:
                return res
        return None


dirs = [POS(0,-1),POS(0,1),POS(-1,0),POS(1,0)]


def create_level():
    l = LEVEL()
    s = LEVEL_SOLVER(l)
    s.solve()
    print("p")
    s.path = s.determine_path()
    print(len(s.path))


if __name__ == '__main__':
    create_level()
