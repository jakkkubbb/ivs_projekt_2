import sys
import math_lib as ml
import random

def main():
    
    
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
    
    with open("./standard_deviation_data/data.txt", "w") as file:
        for _ in range(number):
            value = random.uniform(-1000, 1000)  # Generate random float between -1000 and 1000
            file.write(f"{value}\n")



if __name__ == "__main__":
    main()
