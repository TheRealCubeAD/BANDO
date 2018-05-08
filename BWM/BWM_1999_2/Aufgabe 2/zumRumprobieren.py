
def Q(n):
    s = 0
    while n != 0:
        s += n % 10
        n = int(n / 10)
    return s

for i in range(0,50):
    print(i, 3**i, Q(3**i))