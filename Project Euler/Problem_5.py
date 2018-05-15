x = 20
while 1:
    if all([x % i == 0 for i in range(3, 20)]):
        print(x)  # 232792560
        break
    x += 20

# 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19