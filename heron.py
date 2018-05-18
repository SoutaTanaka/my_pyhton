import math

def heron(a, b, c):
    s = a + b + c
    if g_or_k(s) == True:
        s = s / 2
        a = s - a
        b = s - b
        c = s - c
        s = s*a*b*c
    # if type(math.sqrt(s)) != Double:
    else:
        a = s - a * 2
        b = s - b * 2
        c = s - c * 2
        s = s * a * c * d



def prime(n):
    prime_dict = {}
    x = 0
    while is_prime(int(n)) == False:
        i = 2
        while n % i != 0:
            i += 1
        n = n / i
        bool = i in prime_dict.keys()
        if bool == True:
            x = prime_dict[i]
            prime_dict[i] = x + 1
        elif (not bool == True):
            prime_dict[i] = 1

    bool = n in prime_dict.keys()
    if bool == True:
        x = prime_dict[int(n)]
        prime_dict[int(n)] = x + 1
    elif (not bool == True):
        prime_dict[i] = 1
    return prime_dict






def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1




def g_or_k(n):
    if n % 2 == 0:
        return True
    else:
        return False

#print(heron(int(input()), int(input()), int(input())))


pd = prime(int(input()))
print(pd.items())
