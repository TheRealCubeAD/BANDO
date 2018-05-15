for x in range(998001):
    xx = 998001
    if str(xx) == str(xx)[::-1]:
        for y in range(100,1000):
            z = xx/y
            if z == int(z) and len(str(z)) == 3:
                print(xx)
                exit(0)
