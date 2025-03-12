'''
Maximum difference between two consecutive elements in a list.
Find Maximum Difference Between Two Consecutive Elements (Brute Force Approach)

You are given a list of integers. Write a Python program to find the maximum difference between two consecutive elements in the list using a brute-force approach. The difference is defined as the absolute value of the difference between two consecutive elements.

Parameters:

lst (List of integers): A list of integers.

Returns:

An integer representing the maximum difference between two consecutive elements.

Example:

Input: lst = [1, 7, 3, 10, 5]
Output: 7

The maximum difference is between 3 and 10 (i.e., |3 - 10| = 7).

Input: lst = [10, 11, 15, 3]
Output: 12

The maximum difference is between 15 and 3 (i.e., |15 - 3| = 12).
'''

def max_consecutive_difference(lst):
    # Your code goes here
    
    if len(lst) < 2:
        return 0
    
    maxDifference = 0
        
    for index in range(len(lst)-1):
        diff = lst[index+1]-lst[index]
        if diff < 0:
            diff*=(-1)
            
        if diff > maxDifference:
            maxDifference = diff 
        
    return maxDifference