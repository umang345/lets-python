'''
Description:
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.



Input Parameters:

nums (List[int]): A list of integers where each integer is unique and in the range [0, n].

Output:

int: The missing number in the range [0, n].



Example:

Input: nums = [3, 0, 1]
Output: 2
 
Input: nums = [0, 1]
Output: 2
 
Input: nums = [8, 7, 6, 4, 3, 2, 0, 1]
Output: 5
'''

def find_missing_number(nums):
    """
    Function to find the missing number in the array.
    :param nums: List[int] -> A list of distinct integers in the range [0, n]
    :return: int -> The missing number in the range
    """
    
    ### Approach 1 ###
    # hash = set()
    # for num in range(0, len(nums)+1):
    #     hash.add(num)
        
    # for num in nums:
    #     hash.remove(num)
        
    # return next(iter(hash))
    
    ### aApproach 2 ###
    
    n = len(nums)
    sum = (n*(n+1))//2
    
    for num in nums:
        sum-=num 
        
    return sum