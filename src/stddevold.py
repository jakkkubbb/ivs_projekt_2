"""
@file stddev.py
@brief this file calculates the standard deviation of a list of numbers
@author Marc Bafalluy Gesti 
@author Alex Gajdoš
@author Jakub Miženko
@author Simon Zán
@date 2025-04-24
"""
import cProfile
import sys
import math_lib as ml
import random


def add(data):
    total = 0.0
    for x in data:
        total = ml.sum(total, x)
    return total

def avg(total, n):
    return ml.div(total, n)


def sum_sq_diff(data, avg):
    sum_sq_diff = 0.0
    for x in data:
        diff = ml.sub(x, avg)
        sq = ml.power(diff, 2)
        sum_sq_diff = ml.sum(sum_sq_diff, sq)
    return sum_sq_diff

def stddev(data, n):
    org_sum = add(data)
    calc_mean = avg(org_sum, n)
    up_sum = 0
    up_sum = sum_sq_diff(data, calc_mean)
    stddev = ml.root(2, ml.div(up_sum, ml.sub(n, 1)))
    return f"{stddev:.6f}"



def main():
    """
    @brief main function to calculate the standard deviation of a list of numbers
    @details the function reads a list of numbers from the standard input
    @return the standard deviation of the list of numbers
    """
    
    data = []
    
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

    print(stddev(data, n))


def generate_test_data():
    """
    @brief function to generate test data
    @param number the number of random numbers to generate
    @return the function does not return anything, only generates random numbers
    """

    with open("./standard_deviation_data/data.txt", "w") as file:
        for _ in range(1000):
            value = random.uniform(-1000, 1000)  
            file.write(f"{value}\n")


    with open("./standard_deviation_data/data1.txt", "w") as file1:
        for _ in range(10):
            value = random.uniform(-1000, 1000)  
            file1.write(f"{value}\n")

    with open("./standard_deviation_data/data2.txt", "w") as file2:
        for _ in range(1000000):
            value = random.uniform(-1000, 1000)  
            file2.write(f"{value}\n")


#cProfile.run('main()')
#generate_test_data()



if __name__ == "__main__":
    main()