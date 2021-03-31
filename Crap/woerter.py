import time
from copy import deepcopy
path = "raetsel4.txt"
file = open(path, 'r', encoding='utf-8')

gaps = []
for item in file.readline().rstrip().split():
    for char in (',', '.', '!', '?'):
        item = item.replace(char, '')
    chars = [[i, char] for i, char in enumerate(item) if char != '_']
    chars.append(len(item))
    gaps.append(chars)
words = file.readline().rstrip().split()

def map(words, gaps):
    gap = gaps.pop()
    lenght = gap.pop()
    for word in words:
        if len(word) != lenght:
            continue
        fits = True
        for pos, char in gap:
            if word[pos] != char:
                fits = False
                break
        if fits:
            if len(gaps) == 0:
                return [word]
            else:
                copy = deepcopy(words)
                copy.remove(word)
                res = map(copy, deepcopy(gaps))
                if res != None:
                    res.append(word)
                    return res
    return None

print(map(deepcopy(words), deepcopy(gaps)))
print(time.process_time())
