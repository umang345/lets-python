'''
Description:
You are given a large integer represented as an integer array digits, where each digits[i] is the i-th digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading zeroes.

Write a function to increment the large integer by one and return the resulting array of digits.



Input Parameters:

digits (List[int]): A list of integers where each integer represents a digit of a large number.

Output:

List[int]: The list representing the number after incrementing it by one.



Example:

Input: digits = [1, 2, 3]
Output: [1, 2, 4]
 
Input: digits = [4, 3, 2, 1]
Output: [4, 3, 2, 2]
 
Input: digits = [9, 9, 9]
Output: [1, 0, 0, 0]
'''

def plus_one(digits):
    """
    Function to increment a large integer represented as a list of digits by one.
    :param digits: List[int] -> List of digits representing the large integer
    :return: List[int] -> The list representing the integer after incrementing
    """
    
    if len(digits)==0:
        return [1]
        
    digits[len(digits)-1]+=1
    carry = 0
    
    for index in range(len(digits)-1, -1,-1):
        
        if carry==1:
            digits[index]+=1 
            carry = 0
        
        if digits[index]>9:
            rem = digits[index]%10
            carry = 1 
            digits[index] = rem 
            
    if carry==1:
        digits.insert(0, 1)
        
    return digits