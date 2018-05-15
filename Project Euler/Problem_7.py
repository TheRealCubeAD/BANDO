import sympy

a = 0
i = 1

while a < 10001:
    i += 1
    if sympy.isprime(i) == True:
        a += 1

print(i)