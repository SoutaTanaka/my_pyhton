import time
import random
import numpy as np
from statistics import mean
import matplotlib.pyplot as plt

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def f(x, n):
    return (x**2 + 1) % n

def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

def near_prime(n):
    if is_prime(n) == True:
        return n
    else:
        return near_prime(n + 1)

def row(n):
    a = 2
    b = 2
    d = 1
    while d == 1:
        a = f(a, n)
        b = f(f(b, n), n)
        d = gcd(abs(a - b), n)
    if d == n:
        return False
    else:
        return d

def recursive_prime_factorization(n):
    if n <= 3 :
        return n
    elif is_prime(n) == False:
        m = row(n)
        print(m)
        return recursive_prime_factorization(int(n / m))
    else :
        return (n)

i = 0
a = 3
while i <= 55:
    print(near_prime(a), ",")
    a = near_prime(a) + 1





#print("Please input any number")
#a = input()
#a = near_prime(int(a))
#print("prime1", a)
#print("Please input any number")
#b = input()
#b = near_prime(int(b))
#print("prime2", b)

#def elapsed_time_func (n, m):
#    times=[]
#    for i in range(0, 50):
#        n_prime, m_prime = near_prime(random.randrange(n, m)), near_prime(random.randrange(n, m))
#        start = time.time()
#        row(int(n_prime*m_prime))
#        elapsed_time = time.time() - start
#        times.append(elapsed_time)
#    return(mean(times))
#
#
#
#x = 10
#y = 99
#z = 2
#x_array = []
#y_array = []
#while z < 13:
#    x_array.append(elapsed_time_func(x, y))
#    y_array.append(z)
#    x = x * 10
#    y = y * 10 + 9
#    z += 1
#print("done")
#plt.plot(y_array, x_array)
#plt.show()
#
#


