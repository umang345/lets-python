'''
Description:

Given an array arr of length n, consisting of integers, find the sum of the subarray (including an empty subarray) that has the maximum sum among all possible subarrays.



Input:

An integer array arr of length n where 1 ≤ n ≤ 10^5 and each element arr[i] is an integer.

Output:

An integer representing the sum of the subarray with the maximum sum. If all numbers are negative, the algorithm should handle that correctly by returning the largest single number or zero if the array is empty.

Example:

Input: arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the maximum sum 6.
'''

def max_subarray_sum(arr):
    """
    Given an array of integers, find the maximum sum of any subarray.

    Parameters:
    arr (List[int]): List of integers.

    Returns:
    int: Maximum sum of any subarray.
    """
    
    ### Approach 1 
    
    # if len(arr)==0:
    #     return 0
    
    # maxSum = -float('inf')
    
    # for startIndex in range(len(arr)):
    #     sum = 0
    #     for num in arr[startIndex:]:
    #         sum+=num 
    #         if sum > maxSum:
    #             maxSum = sum 
    
    # return maxSum
    
    ### Approach 2 ###
    
    if len(arr)==0:
        return 0
    
    maxSum = -float('inf')
    currentSum=0
    
    for num in arr:
        currentSum = max(num, currentSum+num)
        maxSum = max(maxSum, currentSum)
        
    return maxSum