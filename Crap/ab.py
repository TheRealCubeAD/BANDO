file = "./wichteln7.txt"
f = open(file, "r")

wishes = []
final_items = []
i = 0
for x in f:
    if i != 0:
        elements = []
        x = x.strip()
        x = x.split(" ")
        for element in x:
            element = element.strip()
            if element.isnumeric():
                elements.append(element)
        wishes.append(elements)
    i += 1

i = 1
while len(wishes) >= i:
    final_items.append([i])
    i += 1
print(final_items)


seen = []
for i, wish in enumerate(wishes):
    if int(wish[0]) in seen:
        print(wish[0], "(first) is in seen")
        if int(wish[1]) in seen:
            print(wish[1], "(second) is in seen")
            if int(wish[2]) in seen:
                print(wish[2], "(third) is in seen")
            else:
                seen.append(int(wish[2]))
                final_items[i].append(int(wish[2]))
        else:
            seen.append(int(wish[1]))
            final_items[i].append(int(wish[1]))
    else:
        seen.append(int(wish[0]))
        final_items[i].append(int(wish[0]))

available = []
i = 1
while len(final_items) >= i:
    if i not in seen:
        available.append(i)
    i += 1

print("seen: ", seen)
print("available: ", available)

def getAndRemoveLastItem(list):
    item = list[-1]
    list.remove(item)
    return item

for item in final_items:
    if len(item) == 1:
        item.append(getAndRemoveLastItem(available))
        print("available: ",available)

print(final_items)




