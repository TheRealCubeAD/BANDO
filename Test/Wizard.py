def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n-1)

def bino(n,k):
    return f(n) / ( f(k) * f(n-k) )

def a(k):
    if len(str(k)) < 2:
        k = str(k)+ " "
    return k

print()
print("Anzahl Spieler:")
s = int(input(">>> "))
print()

for k in range(1, 14):
    print("F",a(k),"", bino(29+k,s-1)/bino(59,s-1)*100)

for k in range(1, 14):
    print("T",a(k),"", bino(42+k,s-1)/bino(59,s-1)*100)