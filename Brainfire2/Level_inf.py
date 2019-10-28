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
        self.conns = [[False for _ in range(4)]for __ in range(4)]

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

    def add_conn(self,start,end):
        self.conns[dirs.index(start)][dirs.index(end)]

    def check(self,room):
        for y in range(4):
            for x in range(4):
                if self.conns[y][x]:
                    if not room.connections[y][x]:
                        return False
        return True




class LEVEL:

    def __init__(self,nsy=8,nsx=8):
        self.sy = nsy
        self.sx = nsx
        self.matrix = [[None for _ in range(self.sx)] for __ in range(self.sy)]
        self.startPos = POS(0,0)
        self.endPos = POS(nsy-1,nsx-1)
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
        self.count = 0



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
            self.place_conns(R, diff)
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


    def place_conns(self, tpl, dir):
        dir_index = dirs.index(dir)
        for i in range(4):
            tpl.conns[i][dir_index] = True


    def determine_path(self):
        self.count = 0
        return self.make_path([],self.level.startPos)


    def make_path(self,path,pos):
        self.count += 1
        if self.count > 1000:
            return
        print(self.count)
        if pos.y not in range(self.level.sy) or pos.x not in range(self.level.sx):
            return None
        if pos in path:
            return None

        path.append(pos)
        if pos == self.level.endPos:
            return path

        if len(path) > int((self.level.sy + self.level.sx)*1.5):
            #return None
            pass

        cur_dirs = copy.deepcopy(dirs)
        random.shuffle(cur_dirs)

        for dir in cur_dirs:
            res = self.make_path(copy.deepcopy(path), pos + dir)
            if res:
                return res
        return None


    def make_path2(self):
        worm = [self.level.startPos]

        while self.level.endPos not in worm:
            A = worm[-1]
            N = [A + dir for dir in dirs if A + dir not in worm and
                 self.in_boarder(A+dir) and self.witdh_search(A+dir,worm)]
            worm.append(random.choice(N))

        return worm



    def witdh_search(self,start,nogos):
        visited = []
        snake = [start]

        while snake:
            item = snake[0]
            del(snake[0])
            if item == self.level.endPos:
                return True
            visited.append(item)
            snake += [item + dir for dir in dirs if item + dir not in nogos
                      and item + dir not in visited and item + dir not in snake and self.in_boarder(item + dir)]

        return False


    def in_boarder(self,pos):
        return pos.y in range(self.level.sy) and pos.x in range(self.level.sx)


    def place_rooms(self):
        snake = []
        for row in self.tpl_mtx:
            snake += row

        while snake:
            rooms = raum.massProduction(1000)
            for room in rooms:
                for tpl in snake:
                    if tpl.check(room):
                        self.level.matrix[tpl.y][tpl.x] = room
                        snake.remove(tpl)


    def place_path(self):
        last_dif = POS(1,0)
        for i in range(len(self.path)-1):
            cur_pos = self.path[i]
            next_pos = self.path[i+1]
            cur_tpl = self.tpl_mtx[cur_pos.y][cur_pos.x]
            dif = next_pos - cur_pos
            cur_tpl.add_conn(last_dif,dif)
            last_dif = dif.invert()


    def prepare_rooms(self):
        for row in self.level.matrix:
            for room in row:
                room.calc_dead_ends()



dirs = [POS(0,-1),POS(0,1),POS(-1,0),POS(1,0)]


def create_level():
    t = time.time()
    dprint("Initializing...")
    l = LEVEL()
    s = LEVEL_SOLVER(l)
    dprint("Making Level retreatable...")
    s.solve()
    dprint("Creating Path to end...")
    s.path = s.make_path2()
    dprint("Length of path: "+str(len(s.path)))
    s.place_path()
    dprint("Placing Rooms...")
    s.place_rooms()
    dprint("Preparing Rooms...")
    s.prepare_rooms()
    dprint("Done!")
    dprint("")
    dprint("Took: "+str(time.time() - t))


def dprint(cont):
    if debug:
        print(cont)
debug = False
if __name__ == '__main__':
    debug = True
    create_level()
