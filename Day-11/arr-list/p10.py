'''
Description:
Given a binary array nums, return the maximum number of consecutive 1s in the array.



Input Parameters:

nums (List[int]): A binary array where each element is either 0 or 1.

Output:

int: The maximum number of consecutive 1s in the array.



Example:

Input: nums = [0, 0, 0, 0]
Output: 0
 
Input: nums = [1, 0, 1, 1, 0, 1, 1, 1, 1]
Output: 4
 
Input: nums = [1, 1, 0, 1, 1, 1]
Output: 3
'''
def find_max_consecutive_ones(nums):
    """
    Function to find the maximum number of consecutive 1's in a binary array.
    :param nums: List[int] -> A binary array where each element is either 0 or 1
    :return: int -> The maximum number of consecutive 1's
    """
    
    maxDuration = 0
    
    start=0
    end=0
    
    while end<len(nums):
        if nums[end]==0:
            duration = end-start 
            if duration>maxDuration:
                maxDuration = duration
            start=end+1
            
        end+=1 
        
    duration = end-start
    if duration>maxDuration:
        maxDuration = duration
        
    return maxDuration    
    
