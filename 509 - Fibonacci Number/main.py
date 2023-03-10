import math

phi = (1 + math.sqrt(5))/2
psi = 1 - phi

# this solution is more than sufficiant for leetcode, however,
# for higher values of n, floating-point error causes the values to be incorrect
def fib(n):
    return round((phi**n)/math.sqrt(5))


# to fix floating-point errors, we can use the decimal module
from decimal import *
phi2 = (1 + Decimal(5).sqrt())/2 
def fib2(n):
    getcontext().prec = 4096
    fn = (Decimal(phi2)**n)/Decimal(5).sqrt()
    return fn.quantize(Decimal('1.'), rounding=ROUND_HALF_UP)


# however, the above solutions are all slow in python due to floating-point math
# using a generator is much faster due to using only integers 
def fib3_gen():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

def fib3(n):
    gen = fib3_gen()
    for i in range(n):
        next(gen)
    return next(gen)


# however, we can get even faster by using a python dictionary (hashmap)
fn = {0:0, 1:1}
def fib4(n):
    if n in fn:
        return fn[n]
    
    else:
        val = fib4(n-1) + fib4(n-2)
        fn[n] = val
        return val


for i in range(5000):
    print(fib4(i))


# with open("./509 - Fibonacci Number/fib.txt") as infile:
#     for i, line in enumerate(infile.readlines()):
#         if fib4(i) != int(line):
#             print("Failed on f({0}): {1} != {2}".format(i, fib(i), line))
#             print("Dif: {}".format(abs(fib(i) - int(line))))
#         else:
#             print("success!", i)