
import random

print()
print("Was ist dein Name?")
name = input(">>> ")
Atacker = {"Sledge":"softbreach","Thatcher":"support","Ash":"softbreach","Thermite":"hardbreach",
           "Twitch":"gadget","Montagne":"support","Glaz":"atack","Fuze":"gadget","Blitz":"atack",
           "IQ":"gadget","Buck":"atack","Blackbeard":"atack","Capitao":"atack","Jackel":"gadget",
           "Ying":"gadget","Zofia":"atack","Doakkaebi":"support","Lion":"support"}

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