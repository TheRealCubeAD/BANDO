
import random

Loesung = [1,2,3,4,5,6,1,2,3,4,5,6]
random.shuffle(Loesung)

for Zahl in Loesung:
    if Loesung.count(Zahl) > 1:
        Loesung.remove(Zahl)

print(Loesung)