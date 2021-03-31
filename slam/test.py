

c = 0
offset = 0
factor = 5
size = 37

buff1 = [0 for _ in range(size)]
buff2 = [0 for _ in range(size)]

while 1:
    for i in range(size):
        c = i
        angle = c * factor + offset
        buff1[c] = angle
    print(buff1)
    for i in range(size):
        c = size - 1 - i
        angle = c * factor + offset
        buff2[c] = angle
    print(buff2)