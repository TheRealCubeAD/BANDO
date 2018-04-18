import math

x = 600851475143
y = int(math.sqrt(x))
while 1:
    if x % y == 0:
        prim = True
        for i in range(1, int((math.sqrt(y)) / 2) + 1):
            if y % (i * 2 + 1) == 0:
                prim = False
                break
        if prim:
            print(y)  # 6857
            break
    y -= 1
