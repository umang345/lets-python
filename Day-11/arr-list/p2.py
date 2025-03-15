'''
Description:
Given a list of integers, write a function to find the sum of all the elements in the list.



Input Parameters:

lst (List[int]): A list of integers.

Output:

int: The sum of all the elements in the list.



Example:

Input: lst = [7]
Output: 7
 
Input: lst = [-1, -2, -3, -4]
Output: -10
 
Input: lst = [1, 2, 3, 4, 5]
Output: 15

'''

def sum_of_elements(lst):
    """
    Function to find the sum of all elements in the list.
    :param lst: List[int] -> List of integers
    :return: int -> The sum of all elements in the list
    """
    
    sum=0
    
    for element in lst:
        sum+=element 
        
    return sum