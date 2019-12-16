import random
class A:
    def __init__(self, i):
        self.x = []
        self.x.append(i)

    def __eq__(self, other):
        return self.x == other.x


a1 = A(1)
a2 = A(2)

f = [a1]

f.index(a2)
