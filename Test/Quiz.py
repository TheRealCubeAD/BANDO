
import random

a = input(">>> ")
b = input(">>> ")
c = input(">>> ")
d = input(">>> ")

print()
print()
print()

L = [a, b, c, d]

for i in range(4):
    o = random.choice(L)
    i = L.index(o)
    del L[i]
    print(o)

