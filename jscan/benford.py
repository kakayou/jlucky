import math

def firstDigital(x):
    while x >= 10:
        x //= 10
    return math.log10(1 + 1/x)

