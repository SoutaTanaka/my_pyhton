import math

#素数判定
def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

#ユークリッドの互除法
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

#引数に一番近い素数を求める
def near_prime(n):
    if is_prime(n) == True:
        return n
    else:
        return near_prime(n + 1)

#二つの引数がお互いに素な数を返す
def each_prime(x, y):
    if y % near_prime(x) == 0:
        return each_prime(x + 1, y)
    else:
        return near_prime(x)

#暗号化、復号化
def key(m, d, n):
    return pow(m, n, d)

#秘密鍵の計算
def find_key(m3, n3):
    v1 = m3
    v2 = n3
    x1 = 1
    x2 = 0
    y1 = 0
    y2 = 1
    while n3 % m3 != 0:
        m1 = n3 % m3
        x3 = x2
        y3 = y2
        x2 = x1 - x2 * math.floor(n3 / m3)
        y2 = y1 - y2 * math.floor(n3 / m3)
        x1 = x3
        y1 = y3
        n3 = m3
        m3 = m1
    if x2 > 0:
        return x2
    elif x2 < 0:
        return x2 + v1




def rsa():
    print("prease input any number")
    n = near_prime(int(input()))
    print("prime1 is", n)

    print("please input any number")
    m = near_prime(int(input()))
    print("prime2 is", m)

    public_key_one = n * m

    intermediate_based = n * m - n - m + 1

    print("Public key1 is", public_key_one)

    print("intermediate based is", intermediate_based)

    print("please input any number")
    public_key_tow = each_prime(int(input()), intermediate_based)
    print("Public key2 is", public_key_tow)

    secret_key = find_key(intermediate_based, public_key_tow)
    print("secret key ia ", secret_key)

    print("Please input Number to encrypt")
    plain_text = int(input())

    encrypted_text = key(plain_text, public_key_one, public_key_tow)
    print("Encrypted text is", encrypted_text)

    decorded_text = key(encrypted_text, public_key_one, secret_key)
    print("Decorded text is", decorded_text)



#print(find_key(3383101552, 24359))
for i in range(0, 10):
    rsa()

















