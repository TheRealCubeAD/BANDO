import random
import time
import raum


class DOOR:  #Hilfsklasse für die Breitensuche
    y = None
    x = None

    successors = []  #Alle von hier aus erreichbaren Knoten
    predecessors = []  #Alle Knoten von denen aus dieser erreichbar ist

    reachable = False  #Ist der Knoten vom Starpunkt aus erreichbar
    retreatable = False  #Ist der Startpunkt von hier erreichbar

    def __init__(self,ny,nx):
        self.y = ny
        self.x = nx


    def append_suc(self, neighbour):  #neuen nachfolger anfügen
        self.successors.append(neighbour)

    def append_pre(self,predecessor):  #neuen vorgänger anfügen
        self.predecessors.append(predecessor)



class LEVEL:
    sy = None  #Grösse in y
    sx = None  #Grösse in x

    matrix = None  #Matrix aus Räumen

    def __init__(self,nsy=6,nsx=6):
        self.sy = nsy
        self.sx = nsx

        rooms = raum.massProduction(self.sy*self.sx)  #Fordere sy*sx räume aus raum.py an

        self.matrix = [rooms[i:i + self.sx] for i in range(0,len(rooms),self.sx)]  #Konvertiere die Liste in eine Matrix



class LEVEL_SOLVER:  #Prüft ob ein Level brauchbar ist:
                # - Der Endpunkt muss vom Startpunkt aus erreichbar sein
                # - Von allen Punkten aus, die vom Startpunkt aus erreichbar sind, muss der Starpunkt erreichbar sein

    level = None  #Referenz auf das zu lösende Level
    sy = None  #Grösse in y
    sx = None  #Grösse in x

    doors = []  #Liste aller Türen

    def __init__(self,nlevel):
        self.level = nlevel
        self.sy = self.level.sy
        self.sx = self.level.sx
        for i in range(2*self.sx*self.sy-self.sx-self.sy):  #Erstelle alle benötigten Türen mit den entsprechenden y,x
            y, x = self.hash_pos(i)
            self.doors.append(DOOR(y, x))


    def hash_index(self,y,x):  #Nimmt eine Position. Gibt den Index in doors der entsprechenden Tür zurück
        if not y % 2:
            res = (x-1)/2 + ((y/2)-1) * self.sx
        else:
            res = ((x/2)-1) + ((y-1)/2) * (self.sx - 1) + self.sx * (self.sy - 1)
        if res != int(res):
            exit("hash_index not int")

        return int(res)


    def hash_pos(self,i):  #Nimmt einen Index in doors. Gibt die Koordinaten der entsprechenden Tür zurück
        if i < self.sx * (self.sy - 1):
            y = 2*(((i-(i%self.sx))/self.sx)+1)
            x = 2*(i%self.sx) + 1
        else:
            y = 2*((i-self.sx*(self.sy-1)-((i-self.sx*(self.sy-1))%(self.sx-1)))/(self.sx-1))+1
            x = 2*(((i-self.sx*(self.sy-1))%(self.sx-1))+1)
        if y != int(y) or x != int(x):
            exit("hash_pos not int")

        return int(y), int(x)


    def build_graph(self):  #Füllt die Adjazenzmatrizen der Türen aus
        for y in range(len(self.level.matrix)):
            for x in range(len(self.level.matrix[y])):
                room = self.level.matrix[y][x]  #Durchlaufe jeden Raum
                my = 1 + 2*y  #berechne den Mittelpunkt des Raums
                mx = 1 + 2*x
                cur_doors = [(my+1,mx,raum.door_down),(my-1,mx,raum.door_up),
                             (my,mx+1,raum.door_right),(my,mx-1,raum.door_left)]  #Berechne alle anliegenden Türen

                for door in cur_doors:
                    if not (self.sy > door[0] > 0 and self.sx > door[1] > 0):
                        cur_doors.remove(door)  #Entferne alle Türen die am Rand liegen
                for d1 in cur_doors:
                    for d2 in cur_doors:
                        if not d1 == d2:  #Durchlaufe alle Tür-Paare

                            #Wenn Tür 2 von Tür 1 aus erreichbar ist, Kannte in Tür 1 eintragen
                            if room.connections[room.IO.index(d1[2])][room.IO.index(d2[2])]:
                                self.doors[self.hash_index(d1[0],d1[1])].append_suc(
                                    self.doors[self.hash_index(d2[0],d2[1])])

                            #Wenn Tür 1 von Tür 2 aus erreichbar ist, Kannte in Tür 1 eintragen
                            if room.connections[room.IO.index(d2[2])][room.IO.index(d1[2])]:
                                self.doors[self.hash_index(d1[0],d1[1])].append_pre(
                                    self.doors[self.hash_index(d2[0],d2[1])])


    def forward_check(self):  #Durchlaufe den Graph in einer Breitensuche und:
                                # - Makiere alle Knoten die vom Start aus erreichbar sind
                                # - Prüfe, ob das Ende vom Start aus erreichbar ist
        visited = []
        snake = [self.doors[0]]

        got_to_end = False

        while snake:
            item = snake[0]
            del(snake[0])
            if not item in visited:
                visited.append(item)
                item.reachable = True
                if item == self.doors[-1]:
                    got_to_end = True
                snake += item.successors

        return got_to_end


    def retreat_check(self):  #Durchlaufe den Graph in einer Breitensuch und:
                                # - Makiere alle Knoten von denen aus der Startpunkt erreichbar ist
                                # - Prüfe dann, ob von allen Knoten aus, die vom Startpunkt aus erreichbar sind,
                                #   der Startpunkt erreichbar ist
        visited = []
        snake = [self.doors[0]]

        while snake:
            item = snake[0]
            del (snake[0])
            if not item in visited:
                visited.append(item)
                item.retreatable = True
                snake += item.predecessors

        for door in self.doors:
            if door.reachable:
                if not door.retreatable:
                    return False

        return True


    def solve_room(self):  #Rufe alle Methoden zur Prüfung des Raumes auf
        self.build_graph()
        print("Graph was build")
        if self.forward_check():
            print("End is reachable")
        else:
            print("End is not reachable")
            return False

        if self.retreat_check():
            print("Retreat works")
            return True
        else:
            print("Retreat does not work")
            return False



if __name__ == '__main__':
    time.clock()
    while 1:
        l = LEVEL(nsy=6, nsx=6)
        s = LEVEL_SOLVER(l)
        if s.solve_room():
            print(time.clock())
            exit()
