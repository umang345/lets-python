'''
Check for anagrams
Problem Description:

You are given two strings s and t. Your task is to determine if string t is an anagram of string s. An anagram is a word or phrase formed by rearranging the characters of a different word or phrase, using all the original characters exactly once.



Input:

Two strings s and t where both lengths are between 1 and 1000.



Output:

Return True if t is an anagram of s, and False otherwise.



Example:

Input: s = "anagram", t = "nagaram"
Output: True
 
Input: s = "rat", t = "car"
Output: False
'''

def is_anagram(s, t):
    """
    Function to check if t is an anagram of s.
    
    Parameters:
    s (str): The first input string.
    t (str): The second input string.
    
    Returns:
    bool: True if t is an anagram of s, False otherwise.
    """
    # Your code here
    
    freq1 = dict()
    freq2 = dict()
    
    for ch in s:
        freq1[ch] = freq1.get(ch,0)+1
        
    for ch in t:
        freq2[ch] = freq2.get(ch,0)+1
        
    if len(freq1.keys()) != len(freq2.keys()):
        return False
        
    for key, val in freq1.items():
        if freq2.get(key,0) != val:
            return False
            
            
    return True