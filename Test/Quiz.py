
import random

a = input(">>> ")
b = input(">>> ")
c = input(">>> ")
D = [a, b, c]
d = random.choice(D)

print()
print()
print()

L = [a, b, c, a, b, c, d]

for i in range(7):
    o = random.choice(L)
    i = L.index(o)
    del L[i]
    print(o)

