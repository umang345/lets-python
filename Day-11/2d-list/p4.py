'''
Description:
You are given two n x n binary matrices mat and target. Your task is to determine whether it is possible to make mat equal to target by rotating mat in 90-degree increments (clockwise). You can rotate mat by 90, 180, or 270 degrees, or leave it unchanged.



Input Parameters:

mat (List[List[int]]): A n x n binary matrix.

target (List[List[int]]): A n x n binary matrix.

Output:

bool: Return True if mat can be made equal to target by rotating it, otherwise return False.



Example:

Input: mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]], target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
Output: True
 
Input: mat = [[0, 1], [1, 1]], target = [[1, 0], [0, 1]]
Output: False
'''

def can_be_rotated(mat, target):
    """
    Function to check if mat can be rotated to match target.
    :param mat: List[List[int]] -> The original matrix
    :param target: List[List[int]] -> The target matrix
    :return: bool -> True if mat can be rotated to match target, otherwise False
    
    
    1  2  3     7  4  1     9  8   7       3  6  9        
    4  5  6     8  5  2     6  5   4       2  5  8
    7  8  9     9  6  3     3  2   1       1  4  7 
    
    
    """
    
    return rotation_0_degree(mat, target) or rotation_90_degree(mat, target) or rotation_270_degree(mat, target) or rotation_180_degree(mat, target)



def rotation_270_degree(mat, target):
    for rowIndex in range(len(mat)):
       for colIndex in range(len(mat)):
           if mat[rowIndex][colIndex] != target[len(mat) - colIndex - 1][len(mat) - rowIndex - 1]:
               return False
    return True
    
def rotation_180_degree(mat, target):
    
    for rowIndex in range(len(mat)):
       for colIndex in range(len(mat)):
           if mat[rowIndex][colIndex]!= target[len(mat)-rowIndex-1][len(mat)-colIndex-1]:
               return False
               
    return True

def rotation_90_degree(mat, target):
    
    for rowIndex in range(len(mat)):
       for colIndex in range(len(mat)):
           
           if mat[rowIndex][colIndex]!= target[colIndex][len(mat)-rowIndex-1]:
               return False
               
    return True
    

def rotation_0_degree(mat, target):
    
    for rowIndex in range(len(mat)):
       for colIndex in range(len(mat)):
           if mat[rowIndex][colIndex]!=target[rowIndex][colIndex]:
               return False
               
    return True
           
           
        
        
    