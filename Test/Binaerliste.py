from copy import deepcopy

def binaerliste(L, n):
    if len(L) < n:
        L.append(0)
        binaerliste(L, n)
        del L[len(L)-1]
        L.append(1)
        binaerliste(L, n)
        del L[len(L) - 1]
    if len(L) == n:
        global ausrichtungKritischerKanten
        M = deepcopy(L)
        ausrichtungKritischerKanten.append(M)

ausrichtungKritischerKanten = []

binaerliste([], 3)
print(ausrichtungKritischerKanten)