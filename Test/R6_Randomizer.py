import random

Attackers = {"Sledge":"softbreach","Thatcher":"support","Ash":"softbreach","Thermite":"hardbreach",
           "Twitch":"gadget","Montagne":"support","Glaz":"attack","Fuze":"gadget","Blitz":"attack",
           "IQ":"gadget","Buck":"attack","Blackbeard":"attack","Capitao":"attack","Hibana":"hardbreach",
           "Jackel":"support","Ying":"gadget","Zofia":"attack","Doakkaebi":"support","Lion":"support",
           "Finka":"support"}
Defenders = {"Doc":"support","Rook":"support","Ela":"entryDenial","Kapkan":"entryDenial","Frost":"entryDenial",
             "Lesion":"entryDenial","Smoke":"entryDenial","Mute":"gadgetDenial","Bandit":"gadgetDenial",
             "Jäger":"gadgetDenial","Vigil":"gadgetDenial","Mira":"fortification","Castle":"fortification",
             "Tachanka":"fortification","Pulse":"intelligence","Echo":"intelligence","Valkyrie":"intelligence",
             "Caveira":"intelligence"}

print()
print("Wie viele Spieler?")
anzahlSpieler = int(input(">>> "))

Spieler = []
for i in range(anzahlSpieler):
    print()
    print("Was ist der Name von Spieler",str(i+1),"?")
    Spieler.append(input(">>> "))

Angreifer = []
Verteidiger = []
for i in Spieler:
    if i == "Alex":
        Angreifer.append(["Sledge", "Thermite", "Dokkaebi", "Finka"])
        Verteidiger.append(["Smoke", "Mute", "Frost"])
    elif i == "Benno":
        Angreifer.append(["Sledge", "Blitz", "Hibana", "Jackal", "Ying"])
        Verteidiger.append(["Smoke", "Tachanka", "Caveira", "Echo"])
    elif i == "Simon":
        Angreifer.append(["Montagne","Fuze","Thermite","Blackbeard"])
        Verteidiger.append(["Mute","Kapkan"])
    elif i == "Andreas":
        Angreifer.append(["Ash","Glaz","Fuze","Lion","IQ","Twitch","Thermite","Blitz","Thatcher"])
        Verteidiger.append(["Echo","Mira","Lesion","Bandit","Jäger","Tachanka","Doc","Smoke"])


alleTeamsAngreifer = []
alleTeamsVerteidiger = []

def alleTeamsAng(L,M):
    l = len(L)
    if l == anzahlSpieler:
        alleTeamsAngreifer.append(L)
    else:
        for i in M[l]:
            L1 = L + [i]
            alleTeamsAng(L1, M)

def alleTeamsDef(L,M):
    l = len(L)
    if l == anzahlSpieler:
        alleTeamsVerteidiger.append(L)
    else:
        for i in M[l]:
            L1 = L + [i]
            alleTeamsDef(L1, M)

alleTeamsAng([],Angreifer)
alleTeamsDef([],Verteidiger)


for i in alleTeamsAngreifer:
    for j in i:
        if i.count(j) != 1:
            alleTeamsAngreifer.remove(i)
            break

for i in alleTeamsVerteidiger:
    for j in i:
        if i.count(j) != 1:
            alleTeamsVerteidiger.remove(i)
            break

def printTeam(T):
    for i in range(anzahlSpieler):
        print(Spieler[i],": ",T[i])

print()
print()
print("Angriff: 'A', Verteidigung: 'V'")

while True:
    print()
    a = input(">>> ")
    if a == "A":
        printTeam(random.choice(alleTeamsAngreifer))
    elif a == "V":
        printTeam(random.choice(alleTeamsVerteidiger))
    else:
        print("Ungültige Eingabe")