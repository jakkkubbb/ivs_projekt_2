

def sum(a, b):
    """
    @brief : function to sum two numbers
    @param a : first number
    @param b : second number
    @return : sum of a and b
    """
    return a + b

def sub(a, b):
    """
    @brief : function to substract the second number from the first
    @param a : first number
    @param b : second number
    @return : result of the subtraction of b from a
    """
    return a - b

def mul(a, b):
    """
    @brief : function to multiply two numbers
    @param a : first number
    @param b : second number
    @return : product of a and b multiplication
    """
    return a * b

def div(a, b):
    """
    @brief : function to divide the first number by the second
    @param a : first number
    @param b : second number
    @return : result of the division of a by b
    @raise ZeroDivisionError : if b is 0
    """
    if b != 0:
        return a / b
    else:
        raise ZeroDivisionError("Division by zero.")
    
def abs_v(a):
    """
    @brief : function to return the absolute value of a number
    @param a : first number
    @return : returns the absolute value of a
    """
    return abs(a)

def power(base, exponent):
    """
    @brief : function to calculate the power of a base raised to an exponent
    @param base : the base number
    @param exponent : the exponent
    @return : result of base raised to the power of exponent
    @raise ValueError : if base is negative and exponent is fractional
    @raise ZeroDivisionError : if base is 0 and exponent is negative
    """
    if base == 0 and exponent < 0:
        raise ZeroDivisionError("0 cannot be raised to a negative power.")
    if base < 0 and not float(exponent).is_integer():
        raise ValueError("Negative base cannot be raised to a fractional power.")
    return base ** exponent

def root(base, root_exponent):
    """
    @brief : function to calculate the root of a number
    @param a : first number
    @param b : second number
    @return : returns the root of base with the given exponent
    """
    if base < 0 and root_exponent % 2 == 0:
        raise ValueError("Cannot compute even root of a negative number.")
    else:
        return base ** (1 / root_exponent)

def factorial(a):
    """
    @brief : function to calculate the factorial of a number
    @param a : the number
    @return : returns the factorial of a
    @raise ValueError : if n is negative
    @raise TypeError : if n is not an integer
    """
    if a < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if type(a) != int:
        raise TypeError("Factorial is only defined for integers.")
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result



