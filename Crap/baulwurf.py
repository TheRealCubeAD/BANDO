import numpy as np
import time
file = open(input("Path: "), 'r')
lenght, hight = int(file.readline()), int(file.readline())
matrix = np.array([[char for char in line.rstrip('\n')] for line in file], dtype=object)
baul = np.array([['X', 'X', 'X'], ['X', ' ', 'X'], ['X', ' ', 'X'], ['X', 'X', 'X']], dtype=object)
count = 0
for y in range(hight - len(baul) + 1):
    for x in range(lenght - len(baul[0]) + 1):
        if np.array_equal(matrix[y:y+len(baul), x:x+len(baul[0])], baul):
            count += 1
print(count)
print(time.process_time())