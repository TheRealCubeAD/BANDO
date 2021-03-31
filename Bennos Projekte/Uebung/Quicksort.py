import random
ran_mode = "min"
count = 0

def quicksort(A, p, r):
    global count
    if p < r - 1:
        if ran_mode == "rand":
            ran = random.randint(p, r)
        elif ran_mode == "low":
            ran = A[p:r].index(min(A[p:r])) + p
        elif ran_mode == "min":
            m = int(sum(A[p:r])/len(A[p:r]))
            ran = A[p]
            for e in A[p:r]:
                if abs(m - e) < abs(m - ran):
                    ran = e
            ran = A.index(ran)

        else:
            ran = 0
        i = partition(A, p, r, ran)
        print(A)
        quicksort(A, p, i)
        quicksort(A, i+1, r)


def partition(A, p, r, t):
    global count
    print(t)
    x = A[t]
    A[t] = A[p]
    i = p
    for j in range(p + 1, r):
        count += 1
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[p] = A[i]
    A[i] = x
    return i


A = [1,5,4,9,4,2]
quicksort(A, 0, 6)
print()
print(A)
print(count)