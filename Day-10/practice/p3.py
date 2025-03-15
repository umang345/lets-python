'''
Selection Sort
Selection Sort Algorithm

You are given a list of integers. Write a Python function to sort the list in ascending order using the Selection Sort algorithm. Selection Sort works by repeatedly finding the minimum element from the unsorted part of the list and swapping it with the first element of the unsorted part.

Parameters:

lst (List of integers): The list to be sorted.

Returns:

A list of integers sorted in ascending order.

Example:

Input: lst = [64, 25, 12, 22, 11]
Output: [11, 12, 22, 25, 64]

Input: lst = [29, 10, 14, 37, 13]
Output: [10, 13, 14, 29, 37]
'''

def selection_sort(arr):
    
    for iteration in range(len(arr)-1):
        minIndex = iteration
        for index in range(iteration+1,len(arr)):
            if arr[index] < arr[minIndex]:
                minIndex = index
        
        temp = arr[iteration]
        arr[iteration] = arr[minIndex]
        arr[minIndex] = temp
        
    return arr
