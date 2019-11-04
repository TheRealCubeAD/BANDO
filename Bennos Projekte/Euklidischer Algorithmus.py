
def euk_alg(a,b):
    s = abs(a)
    t = abs(b)
    while t != 0:
        r = s%t
        s = t
        t = r
        print(s,t,r)
    d = s
    return d


def erw_euk_alg(a,b):
    s = abs(a)
    t = abs(b)
    x = 1
    y = 0
    u = 0
    v = 1
    while t != 0:
        q = int(s/t)
        r = s%t
        s = t
        t = r
        i = x - q*u
        x = u
        u = i
        j = y - q*v
        y = v
        v = j
        print(s,t,q,r,x,y,u,v)

    d = s
    x = sgn(a) * x
    y = sgn(b) * y
    return x,y,d


def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

if __name__ == '__main__':
    #print(euk_alg(int(input("a: ")),int(input("b: "))))
    print(erw_euk_alg(int(input("a: ")),int(input("b: "))))