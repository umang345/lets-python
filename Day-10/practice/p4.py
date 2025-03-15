'''
Insertion Sort
Insertion Sort Algorithm

You are given a list of integers. Write a Python function to sort the list in ascending order using the Insertion Sort algorithm. Insertion Sort works by building a sorted section of the list, one element at a time, by inserting each new element into its proper position within the already sorted section.

Parameters:

lst (List of integers): The list to be sorted.

Returns:

A list of integers sorted in ascending order.

Example:

Input: lst = [12, 11, 13, 5, 6]
Output: [5, 6, 11, 12, 13]

Input: lst = [31, 41, 59, 26, 41, 58]
Output: [26, 31, 41, 41, 58, 59]
'''


def insertion_sort(arr):
    
    for outer in range(len(arr)):
        currentIndex = outer
        check = currentIndex-1
        while check >=0:
            if arr[check] < arr[currentIndex]:
                break 
            check-=1
        
        element = arr[currentIndex]
        swapIndex = currentIndex-1
        while swapIndex > check:
            arr[swapIndex+1] =arr[swapIndex]
            swapIndex-=1
        arr[check+1] = element 

    return arr


lst = [12,11,13,5,6]

arr = insertion_sort(lst)
print(arr)