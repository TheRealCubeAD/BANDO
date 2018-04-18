from math import sqrt

x = 1
y = 3
while x != 10001:
    if all([y % i != 0 for i in range(2, int(sqrt(y) + 1))]):
        x += 1
    y += 2
print(y)  # 104745
