for a in range(899):
    aa = 999 - a
    for b in range(899):
        bb = 999 - a
        x = aa * bb
        if str(x) == str(x)[::-1]:
            print(aa, bb, x)
            exit(0)
