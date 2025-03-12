'''
Check Subsequence
Problem Description:

You are given two strings s and t. Your task is to determine if string t is a subsequence of string s. A subsequence of a string is a new string that is formed from the original string by deleting some (or no) characters without changing the order of the remaining characters.



Input:

Two strings s and t where the length of s is between 1 and 1000, and the length of t is between 1 and 1000.



Output:

Return True if t is a subsequence of s, and False otherwise.



Example:

Input: s = "abcde", t = "ace"
Output: True
 
Input: s = "abcde", t = "aec"
Output: False
'''

def is_subsequence(s, t):
    """
    Function to check if t is a subsequence of s.
    
    Parameters:
    s (str): The original string.
    t (str): The target subsequence string.
    
    Returns:
    bool: True if t is a subsequence of s, False otherwise.
    """
    # Your code here
    
    if len(t) > len(s):
        return False
        
    if len(t)==0:
        return True
        
    for startIndex in range(len(s)):
        if(t[0]==s[startIndex]):
            i=startIndex
            j=0;
            while i < len(s) and j < len(t):
                if s[i]==t[j]:
                    j+=1;
                i+=1 
                
            if j==len(t):
                return True

    return False