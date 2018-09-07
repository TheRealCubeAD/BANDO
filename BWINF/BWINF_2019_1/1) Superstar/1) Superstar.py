
doc = open("superstar"+input("Filenumber: ")+".txt")

teilnehmer = doc.readline().split()
follows = [[] for _ in range(len(teilnehmer))]
for line in doc:
    if line != "\n":
        a,b = line.split()
        follows[teilnehmer.index(a)].append(b)

def request(a,b):
    #  is a following b
    if b in follows[teilnehmer.index(a)]:
        return True
    else:
        return False
