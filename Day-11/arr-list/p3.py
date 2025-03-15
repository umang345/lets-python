'''

Description:
Given a list of integers, write a function to reverse the order of elements in the list.



Input Parameters:

lst (List[int]): A list of integers.

Output:

List[int]: The list with elements in reversed order.



Example:

Input: lst = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
 
Input: lst = [10, 20, 30]
Output: [30, 20, 10]
 
Input: lst = [7, 8, 9]
Output: [9, 8, 7]
'''

def reverse_list(lst):
    """
    Function to reverse the order of elements in a list.
    :param lst: List[int] -> List of integers
    :return: List[int] -> The list with elements in reversed order
    """
    
    start = 0
    end = len(lst)-1
    
    while start <= end :
        tmp = lst[start]
        lst[start] = lst[end]
        lst[end] = tmp
        start+=1 
        end-=1 
        
    return lst