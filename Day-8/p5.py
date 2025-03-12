'''
Decimal to Binary
Problem Description:

You are given an integer n. Your task is to return its binary representation as a string. Do not use any built-in functions for conversion.



Input:

A single integer n, where -10^9 <= n <= 10^9.



Output:

A string representing the binary representation of n.



Example:

Input: n = 5
Output: "101"
 
Input: n = -5
Output: "-101"
'''

def int_to_binary(n):
    """
    Function to convert an integer to its binary representation.
    
    Parameters:
    n (int): The integer to convert.
    
    Returns:
    str: The binary representation of the integer.
    """
    # Your code here

    '''
    10
    5  ->  0 
    2  ->  1 
    1  ->  0 
       ->  1
    '''
    
    num = n
    if (num<0):
        num *= (-1)
        
    temp = list()
    while(num>1):
        temp.append(str(num%2))
        num = int(num/2)
    
    temp.append(str(num))
    temp.reverse()
    
    num_str = "".join(temp)
    if n<0:
        num_str = "-"+num_str
        
    return num_str