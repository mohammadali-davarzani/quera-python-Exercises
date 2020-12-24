from math import *

x = int(input())

first_calculate = ceil(pow(x, 5/3) + tan(radians(x)))
seconde_calculate = floor(pow(pi, 2 + atan(pow(sin(radians(x)), 2))))

output = gcd(first_calculate, seconde_calculate)
print(output)