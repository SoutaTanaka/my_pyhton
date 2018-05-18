import numpy as np
import math
import time



#擬似乱数発生関数
def f(x, c):
    return x**2 + 1 % c

#ユークリッドの互除法を使った最大公約数を求める関数
def gcd(absxy, n):
    while absxy % n != 0:
        k = n
        n = absxy % n
        absxy = k
    return n

#素数判定
def primeDecision(m):
    if m % 2 != 0 and m != 2:
        for i in range(2, int(math.sqrt(m)) + 1):
            if m % i == 0 and m != i:
                return False
                break
        return True
    elif m == 2:
        return True
    else:
        return False


#ポラード・ρ法を使った素因数分解関数
def row(n):
    k = 1
    prime = False
    while prime != True:
        n = n / k
        if primeDecision(n) != True:
            x = 2
            y = 2
            d = 1
            while d == 1:
                x = f(x, n)
                y = f(y, f(y, n))
                d = gcd(abs(x - y), n)
                #print(d)
            if d == n:
                print("Error")
            else:
                if primeDecision(d) == True:
                    print(d)
                    k = d
                else:
                    row(d)
        else:
            prime = True
    print(int(n))



def near_prime(n):
    while primeDecision(n) != True:
        n += 1
    return n



def mend(n):
    for i in range(n):
        i += 2
        if n % i == 0:
            print(n / i)
            print(i)
            break


for i in range(1):
    print("number", i)
    start = time.time()
    row(13 * 11)
    elapsed_time = time.time() - start
    print (format(elapsed_time) + "[sec]")

#291830521
#192876443
#56287232849316803
