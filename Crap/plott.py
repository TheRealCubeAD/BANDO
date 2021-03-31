import math
x = 0
y = 0
l_left = 0
l_right = 0



def calc(left, right):
    global x, y, l_left, l_right

    diff = left - right
    angle = diff * 3.751/2
    forward = ((left - l_left) + (right - l_right))/2
    y += math.cos(angle*3.14159265/180) * forward
    x += math.sin(angle*3.14159265/180) * forward
    l_left = left
    l_right = right
    print(str(x) + ", " + str(y))


l = 0
r = 0

for i in range(100):
    l += 1
    r += 1
    calc(l, r)

for i in range(24):
    l += 1
    r -= 1
    calc(l, r)


for i in range(100):
    l += 1
    r += 1
    calc(l, r)

for i in range(24):
    l += 1
    r -= 1
    calc(l, r)


for i in range(100):
    l += 1
    r += 1
    calc(l, r)

for i in range(24):
    l += 1
    r -= 1
    calc(l, r)


for i in range(100):
    l += 1
    r += 1
    calc(l, r)

for i in range(24):
    l += 1
    r -= 1
    calc(l, r)