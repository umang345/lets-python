'''
Code Bubble Sort
Bubble Sort Algorithm

You are given a list of integers. Write a Python function to sort the list in descending order using the Bubble Sort algorithm. Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated until the list is sorted.

Parameters:

lst (List of integers): The list to be sorted.

Returns:

A list of integers sorted in ascending order.

Example:

Input: lst = [64, 34, 25, 12, 22, 11, 90]
Output: [11, 12, 22, 25, 34, 64, 90]

Input: lst = [5, 1, 4, 2, 8]
Output: [1, 2, 4, 5, 8]
'''

def bubble_sort(lst):
    
    for iteration in range(0, len(lst)-1):
        for index in range(0, len(lst)-1):
            if(lst[index+1]<lst[index]):
                temp = lst[index]
                lst[index] = lst[index+1]
                lst[index+1] = temp
                
    return lst
