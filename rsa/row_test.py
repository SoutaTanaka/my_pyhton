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


n = 0
start=time.time()
row(3696033841)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(5623240003)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(13363484551)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(28440195403)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(45188998447)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(110300732791)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(212657030101)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(468632480881)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(826878709849)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(1715963189779)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(3395403201529)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(6535152784513)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(13188440365813)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(23217368211847)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(44783036906143)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(100235330897833)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(226848595422859)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(452508835294507)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(811209609380767)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(1653850177398619)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(4045870877820151)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(7933929132042937)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(15293116833667219)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(27025934084364031)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(48058780621668643)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(96872884080905827)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(234949257054121891)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(398280398069024467)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(814187131823757301)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(1727443666573050133)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(3743815499030011891)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(5775281147591968027)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1
start=time.time()
row(15247467866184706357)
elapsed_time = time.time() - start
print(elapsed_time)
print(32 + n)
n += 1


