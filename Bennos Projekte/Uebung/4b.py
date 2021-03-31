

def T(n):
    if n == 1:
        return 1
    x = 0
    for i in range(1, n):
        x += T(i)
    return x * 2


def t(n):
    if n <= 2:
        return n
    if n == 3:
        return 6
    return t(n-1) + (t(n-1) - t(n-2))*3

for i in range(1, 1000):
    a = T(i)
    print(i, a, 2*(3**(i-2)))