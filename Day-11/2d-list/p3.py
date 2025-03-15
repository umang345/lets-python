'''
Description:
You are given an m x n matrix. Write a function that returns all the elements of the matrix in spiral order, starting from the top-left corner, moving right across the top row, then down the last column, then left across the bottom row, and then up the first column, repeating this process until all the elements have been visited.



Input Parameters:

matrix (List[List[int]]): A 2D list representing the matrix of size m x n.

Output:

List[int]: A list of integers representing the elements of the matrix in spiral order.



Example:

Input: matrix = [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
 
Input: matrix = [[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
'''

def spiral_order(matrix):
    """
    Function to return the elements of the matrix in spiral order.
    :param matrix: List[List[int]] -> The input matrix
    :return: List[int] -> The elements in spiral order
    
    
    1    2    3    4    5
    6    7    8    9    10
    11   12   13   15   15
    16   17   18   19   20 
    21   22   23   24   25
    26   27   28   29   30
    
    """
    
    top = 0 
    bottom = len(matrix)-1 
    left = 0 
    right = len(matrix[0])-1
    result = list()
    
    
    while top <= bottom and left<=right:
        
        # Left to right
        if top <= bottom and left<=right:
            for index in range(left, right+1):
                result.append(matrix[top][index])
                
            top+=1 
        
        # top to bottom
        if top <= bottom and left<=right:
            for index in range(top, bottom+1):
                result.append(matrix[index][right])
                
            right-=1 
        
        ## right to left
        if top <= bottom and left<=right:  
            for index in range(right, left-1,-1):
                result.append(matrix[bottom][index])
                
            bottom-=1
        
        ## bottom to top
        if top <= bottom and left<=right: 
            for index in range(bottom, top-1,-1):
                result.append(matrix[index][left])
                
            left+=1 
        
    return result
        
        
        
    
    
    
            