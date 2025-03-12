'''
Length of the Longest Word
Problem Description:

You are given a string s. Your task is to find the length of the longest word in the string. A word is defined as a sequence of characters separated by spaces. Do not use any built-in functions for string manipulation.



Input:

A string s, where the length of s is between 1 and 1000 characters.



Output:

An integer representing the length of the longest word in the string.



Example:

Input: s = "The quick brown fox jumps over the lazy dog"
Output: 5
 
Input: s = "Hello World"
Output: 5
'''

def longest_word_length(s):
    """
    Function to find the length of the longest word in a string without using built-in functions.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The length of the longest word.
    """
    
    i=0;
    j=0;
    maxLength = 0
    
    while j < len(s):
        if s[j]==' ':
            current_word_length = j-i
            if maxLength<current_word_length:
                maxLength = current_word_length
            j+=1
            i=j 
        else:
            j+=1 
            
    if i!=j:
        current_word_length = j-i
        if maxLength<current_word_length:
            maxLength = current_word_length
                
    return maxLength