
def eingabe(aus):
    while 1:
        try:
            return int(input(aus))
        except:
            print("Keine gültige Eingabe")

def minrange(cur,lis):
    orderd_lis = []
    for i in range(1,total_range+1):
        if i in lis:
            orderd_lis.append(i)
    curgi = -1
    for i in range(len(orderd_lis)):
        if orderd_lis[i] > cur:
            curgi = i
            break
    if curgi == -1:
        curg = total_range + (total_range-cur)
    else:
        curg = orderd_lis[curgi]
    curki = curgi-1
    if curgi == -1:
        if len(lis)>0:
            curk = orderd_lis[-1]
        else:
            curk = -cur
    else:
        if curki < 0:
            curk = -cur
        else:
            curk = orderd_lis[curki]
    return ((cur+curg)/2)-((cur+curk)/2)
        

def rek(verb,ber):
    bnum = 0
    brange = 0
    bupper = []

    for num in range(1,total_range+1):
        if num not in ber:
            upper = []
            if verb > 0:
                upper,trash = rek(verb-1,ber+[num])
            ran = minrange(num,upper+ber)
            if ran > brange:
                brange = ran
                bnum = num
                bupper = upper
    #print(str(anzahl_spieler-verb),":",bupper,ber,bnum)
    return (bupper + [bnum]), brange

total_range = eingabe("Range: ")
anzahl_spieler = eingabe("Player count: ")
played = []
for z in range(anzahl_spieler):
    print("Calculating...")
    play,pran = rek(anzahl_spieler-(z+1),played)
    print()
    print("Already played:" ,played)
    print("Others will play:", play[:-1])
    print("You should play:", play[-1])
    print("With a range of:", pran)
    print()
    played.append(eingabe(str(z+1)+" plays: "))

proz = []
rang2 = []
for z in range(len(played)):
    rang2.append(minrange(played[z],played[:z]+played[(z+1):]))
    proz.append((rang2[-1]/total_range)*100)
for z in range(len(rang2)):
    print("Player",str(z+1),": took",str(played[z]),"range",str(rang2[z]),"->",str(proz[z])+"%")

                
