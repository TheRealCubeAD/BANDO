import random
import copy
import pprint

def random_mat():
    size = random.randint(3, 10)
    matrix = [[random.choice((True, False)) for _ in range(size)] for __ in range(size)]
    for i in range(size):
        matrix[i][i] = False
    for y in range(size):
        for x in range(size):
            matrix[x][y] = matrix[y][x]
    pprint.pprint(matrix)
    return matrix


def fat(matrix):
    visited = set()
    paths = []
    cost = 0
    d = []



    for i in range(len(matrix)):
        if i not in visited:
            queue = [[i]]
            while queue:
                path = queue.pop(0)

def depth2(matrix):
    visited = set()
    d = []
    cost = 0

    def rek(num):
        nonlocal visited, d, cost
        visited.add(num)
        for nach in [x for x in range(len(matrix)) if matrix[num][x]]:
            if nach in visited:
                continue
            for nachnach in [y for y in range(len(matrix)) if matrix[nach][y]]:
                if nachnach in visited:
                    continue
                cost += 1
                if matrix[nachnach][num]:
                    dr = [num, nach, nachnach]
                    dr.sort()
                    if dr not in d:
                        d.append(dr)

        for nach in [x for x in range(len(matrix)) if matrix[num][x]]:
            if nach not in visited:
                rek(nach)

    for i in range(len(matrix)):
        rek(i)
    print()
    print("DEPTH2:")
    print(d)
    print(len(d))
    print("c:", cost)
    print("-------")
    return len(d), cost


def cont(matrix):
    d = []
    cost = 0
    for i in range(len(matrix)):
        for nach in [x for x in range(len(matrix)) if matrix[i][x]]:
            for nachnach in [y for y in range(len(matrix)) if matrix[nach][y]]:
                cost += 1
                if matrix[nachnach][i]:
                    dr = [i, nach, nachnach]
                    dr.sort()
                    if dr not in d:
                        d.append(dr)

    print("CONT:")
    print(d)
    print(len(d))
    print("c:", cost)
    print("----")
    print()
    return len(d), cost




def test(matrix):
    visited = set()
    d = []
    cost = 0

    def rek(path, num):
        nonlocal visited, matrix, d, cost
        cost += 1
        visited.add(num)
        if len(path) >= 3:
            if path[-3] == num:
                dr = path[-3:]
                dr.sort()
                if dr not in d:
                    d.append(dr)
                return
        if num in path:
            return
        n_path = copy.deepcopy(path)
        n_path.append(num)
        for x in range(len(matrix)):
            if matrix[num][x]:
                rek(n_path, x)

    for i in range(len(matrix)):
        if i not in visited:
            rek([], i)
    print()
    print("DEPTH:")
    print(d)
    print(len(d))
    print(len([1 for x in range(len(matrix)) for y in range(len(matrix)) if matrix[y][x]])/2*len(matrix))
    print("c:", cost)
    print("------")
    print()


for _ in range(1000):
    matrix = random_mat()
    d, c = depth2(matrix)
    dd, cc = cont(matrix)
    if d != dd:
        print("d")
        exit(1)
    if c > len([1 for x in range(len(matrix)) for y in range(len(matrix)) if matrix[y][x]])/2*len(matrix):
        print("c")
        exit(1)