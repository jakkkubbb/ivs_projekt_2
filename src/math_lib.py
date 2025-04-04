import math

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "ERR"
    
def abs_v(n):
    return abs(n)

def power(base, exponent):
    return base ** exponent

def root(base, root_exponent):
    if base < 0 and root_exponent % 2 == 0:
        return "ERR"
    else:
        return math.pow(base, 1/root_exponent)

def factorial(n):
    if n < 0:
        return "ERR"
    if type(n) != int:
        return "ERR"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result



