'''
Description:
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.

The first integer of each row is greater than the last integer of the previous row.

Write a function that takes an integer target and returns True if target is in matrix, or False otherwise. You must solve this problem with a time complexity better than O(m * n).



Input Parameters:

matrix (List[List[int]]): A 2D list representing an m x n matrix.

target (int): The target integer to search for in the matrix.

Output:

bool: Return True if the target is found, otherwise return False.



Example:

Input: matrix = [[1, 3, 5, 7], 
                 [10, 11, 16, 20], 
                 [23, 30, 34, 60]], target = 13
Output: False
 
Input: matrix = [[1, 3, 5, 7], 
                 [10, 11, 16, 20], 
                 [23, 30, 34, 60]], target = 3
Output: True
'''

def search_matrix(matrix, target):
    """
    Function to search for a target in the matrix.
    :param matrix: List[List[int]] -> The input matrix
    :param target: int -> The target value to search for
    :return: bool -> True if target is found, False otherwise
    """
    
    if len(matrix)==0:
        return False
    
    rowIndex = get_row_index(matrix, target)
    
    if rowIndex==-1:
        return False
        
    row = matrix[rowIndex]
    
    start = 0
    end = len(row)-1 
    
    while start<=end:
        mid = start + (end-start)//2
        
        if row[mid]==target:
            return True
        elif row[mid]<target:
            start = mid+1 
        else:
            end = mid-1
            
    return False
    
    
def get_row_index(matrix, target):
    
    row = []
    for index in range(len(matrix)):
        row.append(matrix[0][index])
        
    index = -1
    start = 0
    end = len(row)-1 
    
    while start <= end:
        mid = start + (end-start)//2
        
        if row[mid]==target:
            return mid
        elif row[mid] < target:
            index = mid
            start=mid+1 
        else:
            end = mid-1
            
    return index
