
import random

L = []

while True:
    a = input(">>> ")
    if a == "fertig":
        break
    else:
        L.append(a)

print()
print()
print()


for i in range(len(L)):
    o = random.choice(L)
    i = L.index(o)
    del L[i]
    print(o)