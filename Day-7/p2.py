'''
Largest Element in a List
Find the Largest Element in a List

Write a Python function that finds and returns the largest element in a given list of integers.

Parameters:

numbers (List of integers): The input list containing integers.

Returns:

An integer representing the largest element in the input list.

Example:

Input: numbers = [3, 8, 2, 10, 5]
Output: 10

Input: numbers = [-5, -10, -2, -1, -7]
Output: -1
'''

def find_largest(numbers):
    # Your code goes here
    if len(numbers)==0:
        return 0
        
    largest = numbers[0]
    for num in numbers:
        if largest<num:
            largest = num 
            
    return largest