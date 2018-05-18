from numpy.random import *
import math

def gcd(ina, inb):
    while ina % inb != 0:
        mda = inb
        inb = ina % inb
        ina = mda
    return inb

def fx(up):
    return randint(up)

def primeDecision(m):
    if m % 2 != 0 :
        j = int(math.sqrt(m)) - 3
        for i in range(j):
            i = i + 3
            if m % i == 0:
                return False
                break
    else:
        return False
    return True

def p (n):
    k = 1
    sosuu = False
    while sosuu != True:
        n = n / k
        if primeDecision(n) != True:
            x = 2
            y = 2
            d = 1
            while d == 1:
                x = fx(n)
                y = fx(n)
                d = gcd(abs(x - y), n)
            if d == n:
                print(False)
            else:
                print(int(d))
                k = d
        else:
            sosuu = True
    print(int(n))
    print("Done")


print(p(4853296374))
exit()
