'''
Count consonants in a string
Problem Description:

You are given a string s. Your task is to count the number of consonants in the string and return the total count. A consonant is any alphabetic character that is not a vowel (a, e, i, o, u).



Input:

A single string s, where the length of s is between 1 and 1000.



Output:

An integer representing the total count of consonants in the input string.



Example:

Input: "Hello, World!"
Output: 7
 
Input: "Python Programming"
Output: 13
'''

def count_consonants(s):
    """
    Function to count the number of consonants in the input string.
    
    Parameters:
    s (str): The input string to check for consonants.
    
    Returns:
    int: The count of consonants in the input string.
    """
    # Your code here

    vowels = ['a','e','i','o','u']
    
    result = 0
    
    for ch in s.lower():
        if ch.isalpha() and not ch in vowels:
            result+=1 
            
    return result