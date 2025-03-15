'''
Description:
You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees clockwise. The rotation should be done in-place, meaning you have to modify the input matrix directly without using any additional matrix for storage.



Input Parameters:

matrix (List[List[int]]): A 2D list of integers representing the matrix of size n x n.

Output:

The function should modify the matrix in-place. No need to return anything.
'''

def rotate(matrix):
    """
    Function to rotate the matrix 90 degrees clockwise.
    :param matrix: List[List[int]] -> 2D list representing the matrix
    :return: None -> Modifies the matrix in-place
    """
    transpose(matrix)
    reverseRows(matrix)
    
def reverseRows(matrix):
    for row in matrix:
        start = 0;
        end = len(row)-1
        while start < end :
            tmp = row[start]
            row[start] = row[end]
            row[end] = tmp
            start+=1 
            end-=1 
            
        
    
def transpose(matrix):
    
    diagnol = 0 
    while diagnol < len(matrix):
        for i in range(diagnol, len(matrix)):
            tmp = matrix[diagnol][i]
            matrix[diagnol][i] = matrix[i][diagnol]
            matrix[i][diagnol] = tmp 
        diagnol+=1 
    