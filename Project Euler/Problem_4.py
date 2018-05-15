for x in range(998001):
    xx = 998001 - x
    if str(xx) == str(xx)[::-1]:
        for y in range(100,1000):
            z = xx/y
            if z == int(z) and len(str(int(z))) == 3:
                print(xx) # 913 * 993 = 906609
                exit(0)
