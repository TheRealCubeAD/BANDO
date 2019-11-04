

def b_adisch(B,N):
    k = 0
    x = int(N/B)
    a = N%B

    L = [a]

    while x != 0:
        k += 1
        y = int(x/B)
        a = x%B
        L.append(a)
        x = y

    L.reverse()
    return L

if __name__ == "__main__":
    print(b_adisch(int(input("B >>>")),int(input("N >>>"))))
