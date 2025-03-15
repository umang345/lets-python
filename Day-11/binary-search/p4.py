'''
Description:
Given a sorted array that has been rotated, find the minimum element in the array. The array was originally sorted in ascending order and then rotated at some pivot.



Parameters:

nums (List[int]): A list of integers sorted in ascending order but rotated at an unknown pivot.

Return Values:

int: The minimum element in the rotated sorted array.



Example:

Input: nums = [4, 5, 6, 7, 0, 1, 2] 
Output: 0 
Explanation: The minimum element is 0.
 
Input: nums = [11, 13, 15, 17] 
Output: 11 
Explanation: The array was not rotated, and the minimum element is the first element.

'''

def findMin(nums):
    
    # [4 5 6 7 0 1 2]
    
    # if nums[start] < nums[mid] < nums[end]  => return nums[start]
    
    # if nums[mid] > nums[end]  =>  start = mid+1 
    
    # [6 7 0 1 2 3 4 5]  if nums[mid] < nums[end]  => end = mid-1
    
    start = 0
    end = len(nums)-1 
    
    resut = -1
    
    while start <= end:
        mid = start + (end-start)//2
        
        if nums[start]<=nums[mid] and nums[mid] <= nums[end]:
            result =  nums[start]
            break
        
        elif nums[mid] > nums[end]:
            start = mid+1
        else:
            end = mid-1
            
    
    return result
