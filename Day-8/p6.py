'''
Binary to Decimal
Problem Description:

You are given a string binary_str representing a binary number. Your task is to convert this binary string to its corresponding decimal integer. Do not use any built-in functions for conversion.



Input:

A string binary_str, consisting of characters '0' and '1', where the length of the string is between 1 and 30 (inclusive).



Output:

An integer representing the decimal value of the binary string



Example:

Input: binary_str = "101"
Output: 5
 
Input: binary_str = "1101"
Output: 13

'''

def binary_to_decimal(binary_str):
    """
    Function to convert a binary string to its decimal integer representation.
    
    Parameters:
    binary_str (str): The binary string to convert.
    
    Returns:
    int: The decimal representation of the binary string.
    """
    # Your code here
    
    result = 0
    weight = 1
    
    for digit_char in binary_str[::-1]:
        
        if digit_char == '1':
            result+=weight
        weight *= 2
            
    return result