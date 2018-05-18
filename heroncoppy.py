import math

def heron(a, b, c):
    s = a + b + c
    s = float(s) / 2
    a = s - a
    b = s - b
    c = s - c
    return math.sqrt(s*a*b*c)

print(heron(float(input()), float(input()), float(input())))
