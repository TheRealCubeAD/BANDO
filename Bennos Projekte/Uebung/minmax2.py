import math
eqs = 0

def minmax(items):
    global eqs
    if len(items) == 2:
        eqs += 1
        if items[0] < items[1]:
            return items[0], items[1]
        else:
            return items[1], items[0]
    else:
        min1, max1 = minmax(items[:len(items)//2])
        min2, max2 = minmax(items[len(items)//2:])
        eqs += 1
        if min1 < min2:
            min = min1
        else:
            min = min2

        eqs += 1
        if max1 > max2:
            max = max1
        else:
            max = max2
        return min, max

def run(n):
    global eqs
    eqs = 0
    l = [i for i in range(n)]
    minmax(l)
    return eqs

for n in range(1, 10):

    i = 2**n

    x = 0
    for y in range(int(math.log(i, 2)-2)):
        x += 2**y
    x*=2
    x += i
    x = int(x)
    print(x, 2 * (i - 1), run(i))