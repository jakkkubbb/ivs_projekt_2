"""
@file stddev.py
@brief this file calculates the standard deviation of a list of numbers
@author Marc Baffaluy Gesti 
@author Alex Gajdoš
@author Jakub Miženko
@author Simon Zán
@date 2025-04-24
"""

import sys
import math_lib as ml
import random

def main():
    """
    @brief main function to calculate the standard deviation of a list of numbers
    @details the function reads a list of numbers from the standard input
    @return the standard deviation of the list of numbers
    """
    
    data = []

    #generate_test_data(1000)  # Generate 1000 random numbers for testing
    
    
    for line in sys.stdin:
        for item in line.strip().split():
            try:
                number = float(item)
                data.append(number)
            except ValueError:
                continue

    

    
    n = len(data)
    if n < 2:
        print("Atleast 2 numbers are required to calculate the standard deviation.")
        return

    


    total = 0.0
    for x in data:
        total = ml.sum(total, x)
    avg = ml.div(total, n)

    
    sum_sq_diff = 0.0
    for x in data:
        diff = ml.sub(x, avg)
        sq = ml.power(diff, 2)
        sum_sq_diff = ml.sum(sum_sq_diff, sq)

    
    stddev = ml.root(2, ml.div(sum_sq_diff, ml.sub(n, 1)))
    print(f"Standard deviation is: {stddev:.6f}")




def generate_test_data(number):
    """
    @brief function to generate test data
    @param number the number of random numbers to generate
    @return the function does not return anything, only generates random numbers
    """

    with open("./standard_deviation_data/data.txt", "w") as file:
        for _ in range(number):
            value = random.uniform(-1000, 1000)  # Generate random float between -1000 and 1000
            file.write(f"{value}\n")



if __name__ == "__main__":
    main()
