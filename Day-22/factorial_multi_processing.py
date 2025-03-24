import multiprocessing
import math 
import sys
import time 

# sys.set_int_max_str_digits(100000)

## funtion to compute factorial of a given number 

def compute_factorial(number):

    print(f"Computing factorial of a number {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":

    numbers = [5000, 6000, 700, 8000]

    start_time = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()
    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")