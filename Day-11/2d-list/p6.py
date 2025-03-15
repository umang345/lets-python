'''
Description:
In MATLAB, there is a handy function called reshape that reshapes a matrix of dimensions m x n into a new one with a different size r x c keeping its original data in row-traversing order.

You are given an m x n matrix mat and two integers r and c representing the number of rows and columns of the wanted reshaped matrix. The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with the given parameters is possible and legal, output the new reshaped matrix. Otherwise, output the original matrix.



Input Parameters:

mat (List[List[int]]): A 2D list representing an m x n matrix.

r (int): The number of rows for the reshaped matrix.

c (int): The number of columns for the reshaped matrix.



Output:

List[List[int]]: The reshaped matrix or the original matrix if reshaping isn't possible.



Example:

Input: mat = [[1, 2], [3, 4]], r = 1, c = 4
Output: [[1, 2, 3, 4]]
 
Input: mat = [[1, 2], [3, 4]], r = 2, c = 4
Output: [[1, 2], [3, 4]]
'''

def matrix_reshape(mat, r, c):
    """
    Function to reshape a matrix.
    :param mat: List[List[int]] -> The original matrix
    :param r: int -> Number of rows in reshaped matrix
    :param c: int -> Number of columns in reshaped matrix
    :return: List[List[int]] -> The reshaped matrix or original matrix if not possible
    """
    
    linear = list()
    
    for row in mat:
        for col in row:
            linear.append(col)
            
    if r*c != len(linear):
        return mat

    k = 0
    
    result = list()
    
    for rowIndex in range(r):
        row = list()
        for colIndex in range(c):
            row.append(linear[k])
            k+=1 
        result.append(row)
        
    return result