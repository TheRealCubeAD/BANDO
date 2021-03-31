


def heap_sort(A):
    heapify(A)
    for k in range(len(A)-1):
        j = len(A) - k
        A[0], A[j-1] = A[j-1], A[0]
        print(A)
        sift_down(A,0,j-2)


def sift_down(A, i, j):
    while(1):
        k = 2 * i + 1
        if k > j:
            break
        if k < j and A[k+1] < A[k]:
            k += 1
        if A[i] > A[k]:
            A[i], A[k] = A[k], A[i]
            print(A)
            i = k
        else:
            break

def heapify(A):
    print("h")
    n = len(A)
    for k in range(int(n/2)):
        i = int(n/2) - k - 1
        sift_down(A, i, n-1)
    print("end h")


A = [1,5,4,9,4,2]
heap_sort(A)
print(A)