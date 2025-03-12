'''
Sum of N Even Natural Numbers
Problem Description:

You are given an integer n. Your task is to calculate and return the sum of the first n even natural numbers. The even natural numbers are: 2, 4, 6, 8, ...



Input:

A single integer n where 1 <= n <= 10^4.



Output:

Return the sum of the first n even natural numbers.



Example:

Input: n = 3
Output: 12  # (2 + 4 + 6)
 
Input: n = 5
Output: 30  # (2 + 4 + 6 + 8 + 10)
'''

def sum_of_even_numbers(n):
    """
    Function to return the sum of the first n even natural numbers.
    
    Parameters:
    n (int): The number of even numbers to sum.
    
    Returns:
    int: The sum of the first n even natural numbers.
    """
    # Your code here
    
    even_sum = 0
    currentEvenNumber = 0
    currentCount = 0
    
    while currentCount < n:
        currentEvenNumber+=2
        even_sum+=currentEvenNumber
        currentCount+=1 
        
    return even_sum
    