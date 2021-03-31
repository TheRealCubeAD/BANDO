

def mult(x, y):
    result = 0
    for i in range(len(y)):
        r = 0
        for j in range(len(x)):
            r += (10**j) * (int(x[len(x) - j - 1]) * int(y[len(y) - i - 1]))
        result += (10**i) * (r)
    return result

print(mult(input("x: "), input("y: ")))