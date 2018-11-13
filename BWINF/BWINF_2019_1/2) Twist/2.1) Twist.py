import random
from copy import deepcopy

doc = open("twist"+input("Filename: ")+".txt")
text = []
for line in doc:
    text += line.split()

text2 = []

for word in text:
    word2 = list(word)
    for char in word2:
        if not char.isalpha():
            word2.remove(char)
    if word2 != []:
        text2.append(word2)

print(text)
print(text2)