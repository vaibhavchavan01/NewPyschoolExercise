
from functools import reduce


def factorial(num):
    start = 9
    return reduce(lambda x,y:x*y ,range(1, num), start) 
print(factorial(9))