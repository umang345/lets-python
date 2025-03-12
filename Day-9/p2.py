'''
Count Vowels in a string
Problem Description:

You are given a string s. Your task is to count the number of vowels (both uppercase and lowercase) in the string and return the total count.



Input:

A single string s, where the length of s is between 1 and 1000.



Output:

An integer representing the total count of vowels in the input string.



Example:

Input: "Hello, World!"
Output: 3
 
Input: "Python Programming"
Output: 4
'''

def count_vowels(s):
    """
    Function to count the number of vowels in the input string.
    
    Parameters:
    s (str): The input string to check for vowels.
    
    Returns:
    int: The count of vowels in the input string.
    """
    # Your code here
    
    count = 0
    
    s = s.lower()
    vowels = ['a','e','i','o','u']
    
    for ch in s:
        if ch in vowels:
            count+=1
    
    return count
    