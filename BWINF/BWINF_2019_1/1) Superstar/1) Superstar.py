from copy import deepcopy
import random
import time

def index(per):
    return teilnehmer.index(per)

def noStar():
    print("Es gibt keinen SuperStar in dieser Gruppe.")
    print("Das hat sie", reqCount, "Euro gekostet.")
    print("Laufzeit:", str(time.process_time()), "s")
    exit(0)

def Star():
    print("Es wurde ein SuperStar gefunden:",possibleStar)
    print("Das hat sie",reqCount,"Euro gekostet.")
    print("Laufzeit:", str(time.process_time()), "s")
    exit(0)

doc = open("superstar"+input("Filenumber: ")+".txt")
print()
teilnehmer = doc.readline().split()
follows = [[] for _ in range(len(teilnehmer))]
for line in doc:
    if line != "\n":
        a,b = line.split()
        follows[index(a)].append(b)

def request(a,b):
    global reqCount
    #  is a following b
    reqCount += 1
    if b in follows[index(a)]:
        return True
    else:
        return False

reqCount = 0
revealMatrix = [ [-1 for _ in range(len(teilnehmer))] for _ in range(len(teilnehmer))]
possibleStars = deepcopy(teilnehmer)

while(len(possibleStars) >= 2):
    perA = random.choice(possibleStars)
    possibleStars.remove(perA)

    perB = random.choice(possibleStars)
    possibleStars.remove(perB)

    AfollowsB = request(perA,perB)

    revealMatrix[ index(perA) ][ index(perB) ] = AfollowsB
    if AfollowsB:
        possibleStars.append(perB)
    else:
        possibleStars.append(perA)

possibleStar = possibleStars[0]

needRequests = []
for i in range(len(teilnehmer)):
    if i != index(possibleStar):
        if revealMatrix[index(possibleStar)][i] == -1:
            needRequests.append((possibleStar,teilnehmer[i],False))
        if revealMatrix[i][index(possibleStar)] == -1:
            needRequests.append((teilnehmer[i],possibleStar,True))

while len(needRequests) > 0:
    curReq = random.choice(needRequests)
    needRequests.remove(curReq)
    if request(curReq[0],curReq[1]) != curReq[2]:
        noStar()

Star()

