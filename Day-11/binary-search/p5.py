'''
Description:
Given a sorted array that has been rotated, find the index of a given target value. The array was originally sorted in ascending order and then rotated at some pivot.



Parameters:

nums (List[int]): A list of integers sorted in ascending order but rotated at an unknown pivot.

target (int): The integer value to search for in the array.

Return Values:

int: The index of the target value in the array, or -1 if the target is not in the array.



Example:

Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0 
Output: 4 
Explanation: The target value 0 is at index 4 in the rotated array.
 
 
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3 
Output: -1 
Explanation: The target value 3 is not present in the array.
'''

def search(nums, target):
    
    
    '''
    [0 1 2 3 4 5 6 7]
    
    [6 7 0 1 2 3 4 5]
    
    [3 4 5 6 7 0 1 2]
    
    // If number does not exist, return -1
    
    // nums[start] <= nums[mid] <= nums[end]   range is sorted  (regular BS)
    
    // nums[mid] >= nums[start] and nums[mid] >= nums[end]
    // if target nums[start],nums[mid]   ---> BS(left half)
    // else start = mid+1 
    
    // nums[mid] <= nums[start] and nums[mid] <= nums[end]
    // if target in nums[mid],nums[end]   ---> BS(right half)
    // else end = mid-1
    
    '''
    
    start = 0
    end = len(nums)-1 
    
    while start <= end :
        mid = start + (end-start)//2
        
        if nums[start] <= nums[mid] and nums[mid] <= nums[end]:
            if nums[mid]==target:
                return mid 
            elif nums[mid]>target:
                end = mid-1
            else:
                start = mid+1 
        elif nums[start] <= nums[mid] and nums[end] <= nums[mid]:
            if target>=nums[start] and target<=nums[mid]:
                end = mid 
            else:
                start = mid+1 
        else:
            if target >= nums[mid] and target <=nums[end]:
                start = mid 
            else:
                end = mid-1
                
    return -1