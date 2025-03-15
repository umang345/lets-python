'''
Description:
You are given a sorted array of characters letters, sorted in non-decreasing order, and a character target. There are at least two different characters in letters. Your task is to return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.



Input:

letters: A sorted array of characters in non-decreasing order.

target: A character to compare against.

Output:

Return the smallest character that is greater than target. If no such character exists, return the first character in letters.



Example:

Input:
letters = ['c', 'f', 'j']
target = 'k'
Output: 'c'
 
Input:
letters = ['c', 'f', 'j']
target = 'c'
Output: 'f'
 
Input:
letters = ['c', 'f', 'j']
target = 'a'
Output: 'c'
'''

def next_greatest_letter(letters, target):
    """
    Return the smallest character in letters that is lexicographically greater than target.

    Parameters:
    letters (List[char]): Sorted array of characters.
    target (char): The target character.

    Returns:
    char: The smallest character greater than target, or the first character if no such character exists.
    """
    
    index = -1
    
    start = 0;
    end = len(letters)-1
    
    while start <= end :
        mid = start + (end-start)//2
        
        if letters[mid]>target:
            index = mid
            end = mid-1
        elif letters[mid]<=target:
            start = mid+1
            
    if index==-1:
        return letters[0]
        
    return letters[index]
            
