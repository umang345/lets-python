'''
Rotate a List (Without Slicing)

You are given a list of integers and an integer k. Write a Python function to rotate the list to the right by k positions without using slicing. A rotation shifts elements from the end of the list to the front.

Parameters:

lst (List of integers): The list to be rotated.

k (Integer): The number of positions to rotate the list.

Returns:

A list of integers rotated by k positions.

Example:

Input: lst = [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]

Input: lst = [10, 20, 30, 40, 50], k = 3
Output: [30, 40, 50, 10, 20]
'''

def rotate_list(lst, k):
    # Your code goes here
    
    if len(lst) == 0:
        return list()
    
    actual_rotations = k % len(lst)
    
    '''
    1 2 3 4 5 6 7 8      k = 3
    
    8 1 2 3 ..
    7 8 1 2 3..
    6 7 8 1 2 3...
    '''
    
    rotated_list = list()
    
    for index in range(len(lst)-actual_rotations , len(lst)):
        rotated_list.append(lst[index])
        
    for index in range(len(lst)-actual_rotations):
        rotated_list.append(lst[index])
        
    return rotated_list