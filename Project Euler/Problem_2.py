f1, f2 = 1, 1
res = 0
f3 = 0
while f3 < 4000000:
    if f3 % 2 == 0:
        res += f3
    f3 = f2 + f1
    f1 = f2
    f2 = f3
print(res)  # 4613732
