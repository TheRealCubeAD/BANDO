from copy import deepcopy

class x:
    a = 1

x1 = x()
x2 = deepcopy(x1)
x1.a = 2
print(x2.a)