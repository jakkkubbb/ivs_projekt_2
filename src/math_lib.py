"""
@file math_lib.py
@brief This file contains our custom math library with basic operations
@details The library includes functions for addition, subtraction, multiplication,
        division, absolute value, power, root, and factorial.
@author Marc Bafalluy Gesti 
@author Alex Gajdoš
@author Jakub Miženko
@author Simon Zán
@date 2025-04-20

"""


def sum(a, b):
    """
    @brief function to sum two numbers
    @param a first number
    @param b second number
    @return sum of a and b
    """
    return a + b

def sub(a, b):
    """
    @brief function to substract the second number from the first
    @param a first number
    @param b second number
    @return subtraction of b from a
    """
    return a - b

def mul(a, b):
    """
    @brief function to multiply two numbers
    @param a first number
    @param b second number
    @return product of a and b multiplication
    """
    return a * b

def div(a, b):
    """
    @brief function to divide the first number by the second
    @param a first number
    @param b second number
    @return result of the division of a by b
    @exception ZeroDivisionError : if b is 0
    """
    if b != 0:
        return a / b
    else:
        raise ZeroDivisionError("Division by zero.")
    
def abs_v(a):
    """
    @brief function to return the absolute value of a number
    @param a first number
    @return absolute value of a
    """
    return abs(a)

def power(base, exponent):
    """
    @brief function to calculate the power of a base raised to an exponent
    @param base the base number
    @param exponent the exponent
    @return result of base raised to the power of exponent
    @exception ValueError if base is negative and exponent is fractional
    @exception ZeroDivisionError if base is 0 and exponent is negative
    """
    if base == 0 and exponent < 0:
        raise ZeroDivisionError("0 cannot be raised to a negative power.")
    if base < 0 and not float(exponent).is_integer():
        raise ValueError("Negative base cannot be raised to a fractional power.")
    return base ** exponent

def root(root_exponent, base):
    """
    @brief function to calculate the root of a number
    @param base base number
    @param root_exponent the root exponent
    @return the root of base with the given exponent
    """
    if root_exponent == 0:
        return "ERR"  
    if base < 0 and root_exponent % 2 == 0:
        return "ERR"  
    if base == 0 and root_exponent < 0:
        return "ERR"  
    if base < 0 and root_exponent % 2 != 0:
        return -((-base) ** (1 / root_exponent))  
    return base ** (1 / root_exponent)

def factorial(a):
    """
    @brief function to calculate the factorial of a number
    @param a the number to be factorialized
    @return the factorial of a
    @exception ValueError : if n is negative
    @exception TypeError : if n is not an integer
    """
    if a < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if type(a) != int:
        raise TypeError("Factorial is only defined for integers.")
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result



