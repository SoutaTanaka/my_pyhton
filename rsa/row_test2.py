import time
import random
from statistics import mean

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


n = 65
start=time.time()
row(24179827460274905899)
elapsed_time = time.time() - start
print(elapsed_time)
print(n)
n += 5
start=time.time()
row(789447705299158730689)
elapsed_time = time.time() - start
print(elapsed_time)
print(n)
n += 5
start=time.time()
row(26103327120382927283971)
elapsed_time = time.time() - start
print(elapsed_time)
print(n)
n += 5
start=time.time()
row(949362536656351872114787)
elapsed_time = time.time() - start
print(elapsed_time)
print(n)
n += 5
start=time.time()
row(33121113662804190062433067)
elapsed_time = time.time() - start
print(elapsed_time)
print(n)
n += 5
start=time.time()
row(869767422195191496280269781)
elapsed_time = time.time() - start
print(elapsed_time)
print(n)
n += 5
start=time.time()
row(30337184213942566470644541493)
elapsed_time = time.time() - start
print(elapsed_time)
print(n)
n += 5
start=time.time()
row(1073508497867747578202283876493)
elapsed_time = time.time() - start
print(elapsed_time)
print(n)
n += 5
