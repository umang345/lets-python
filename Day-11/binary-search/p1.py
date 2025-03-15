'''
Description:
You are given an m x n matrix grid where each row and column is sorted in non-increasing order. Your task is to return the number of negative numbers present in the matrix.



Parameters:

grid (List[List[int]]): A 2D matrix with dimensions m x n, where each row and each column is sorted in non-increasing order.

Return Values:

Integer: The count of negative numbers in the matrix.



Example:

Input: grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]] 
Output: 7 
Explanation: There are 7 negative numbers in the matrix.
 
Input: grid = [[3, 2], [1, 0]] 
Output: 0 
Explanation: There are no negative numbers in the matrix.
'''

def countNegatives(grid):
    
    count = 0
    
    for row in grid:
        count += countNegativeNumberInRow(row) 
    return count
    
def countNegativeNumberInRow(row):
    
    start = 0
    end = len(row)-1
    index = -1
    
    while start <= end:
        mid = start + (end-start)//2
        
        if row[mid] < 0:
            index = mid
            end = mid-1
        else:
            start = mid+1 
            
    if index == -1:
        return 0
        
    return len(row) - index
        