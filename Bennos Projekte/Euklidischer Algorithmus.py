def sam(y, k, n):
    x = 1
    while k != 0:
        if k%2 != 0:
            x = (x*y) %n
            k = k-1
        y = (y**2) %n
        k /= 2
        print(x, y, k)
    return x

def modInv(a, m):
    (ggt, x, y) = erw_euk_alg(a, m)
    if ggt > 1:
        return -1
    else:
        if x < 0:
            x = x + m
        return x

def erw_euk_alg(a,b):
    aalt = a
    amitte = b
    xalt = 1
    xmitte = 0
    yalt = 0
    ymitte = 1
    while amitte != 0:
        q = aalt // amitte
        aneu = aalt - q * amitte
        xneu = xalt - xmitte * q
        yneu = yalt - ymitte * q
        xalt = xmitte
        xmitte = xneu
        yalt = ymitte
        ymitte = yneu
        aalt = amitte
        amitte = aneu
        print(amitte, ' = ', xmitte, ' * ', a, ' + ', ymitte, ' * ', b)
    return (aalt, xalt, yalt)


def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

if __name__ == '__main__':
    inp = int(input(">>>"))
    if inp == 1:
        print(erw_euk_alg(int(input("a: ")),int(input("b: "))))
    if inp == 2:
        print(modInv(int(input("a: ")), int(input("modulo: "))))
    if inp == 3:
        print(sam(int(input("Basis: ")), int(input("Exponent: ")), int(input("modulo: "))))
        
