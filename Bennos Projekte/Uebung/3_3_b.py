

def rus_mult(x, y):
    res = 0
    while y > 0:
        if y%2 == 1:
            res += x
        y = int(y/2)
        x *= 2
    return res

print(rus_mult(int(input("x: ")), int(input("y: "))))