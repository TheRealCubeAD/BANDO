
import random

print()
print("Was ist dein Name?")
name = input(">>> ")
Atacker = {"Sledge":"softbreach","Thatcher":"support"}

if name == "Alex":
    Angreifer = ["Sledge", "Thermite", "Dokkaebi", "Finka"]
    Verteidiger = ["Smoke", "Mute", "Frost"]
elif name == "Benno":
    Angreifer = ["Sledge", "Blitz", "Hibana", "Jackal", "Ying"]
    Verteidiger = ["Smoke", "Tachanka", "Caveira", "Echo"]

print()
print("Angreifer: 'A', Verteidiger: 'V'")

while True:
    print()
    i = input(">>> ")
    if i == "A":
        print(random.choice(Angreifer))
    elif i == "V":
        print(ramdom.choice(Verteidiger))