'''
Check if All Elements in a List are Unique

You are given a list of integers. Write a Python program that checks if all elements in the list are unique. If all elements are unique, return True; otherwise, return False.

Parameters:

lst (List of integers): The list of integers to check for uniqueness.

Returns:

A boolean value True if all elements in the list are unique, False otherwise.

Example:

Input: lst = [1, 2, 3, 4, 5]
Output: True

Input: lst = [1, 2, 3, 3, 4, 5]
Output: False
'''

def check_unique_1(lst):
    # Manual Method
    
    tracker = set()
    for element in lst:
        if element in tracker:
            return False 
        tracker.add(element)
        
    return True



def check_unique_2(lst):
    lst.reverse()
    return lst
    # Original list modified 

def check_unique_3(lst):

    reversed_list = lst.reversed()
    return reversed_list
    # Original List not updated

def check_unique_4(lst):

    start = 0, end = len(lst)-1
    while start < end :
        tmp = lst[start]
        lst[start] = lst[end]
        lst[end] = tmp 
        start+=1
        end-=1

    return lst