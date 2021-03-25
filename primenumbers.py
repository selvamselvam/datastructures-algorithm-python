
class MyEmptyClass:
    pass

def prime_numbers():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
            else:
                print( str(x) + " is a prime number")



prime_numbers()

import os
print(os.getcwd())
dir(os)

import math
math.cos(math.pi / 4)

import random
print(random.choice(['1','2','3','4']))