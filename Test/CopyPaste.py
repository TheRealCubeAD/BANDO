
text = open("testtext.txt", "r")

L = []

for line in text:
    L.append( line.rstrip() )


text.close()

L.sort()

for i in L:
    print(i)

