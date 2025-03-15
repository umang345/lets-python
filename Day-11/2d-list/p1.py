'''
Description:
Given an integer numRows, return the first numRows of Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it. The first row is row 0, which is [1].



Input Parameters:

numRows (int): The number of rows of Pascal's triangle to generate.

Output:

List[List[int]]: A list of lists where each list represents a row in Pascal's triangle.



Example:

Input: numRows = 3
Output: [
  [1],
  [1, 1],
  [1, 2, 1]
]
 
Input: numRows = 1
Output: [
  [1]
]
 
Input: numRows = 5
Output: [
  [1],
  [1, 1],
  [1, 2, 1],
  [1, 3, 3, 1],
  [1, 4, 6, 4, 1]
]

'''

def generate(numRows):
    """
    Function to generate the first numRows of Pascal's triangle.
    :param numRows: int -> Number of rows of Pascal's triangle to generate
    :return: List[List[int]] -> The first numRows of Pascal's triangle
    """
    
    result = list()
    
    for row in range(numRows):
        if row==0:
            result.append([1])
        else:
            lastRow = result[len(result)-1]
            lastRowLength = len(result[len(result)-1])
            currentRow = list()
            for index in range(lastRowLength+1):
                if index==0 or index==lastRowLength:
                    currentRow.append(1)
                else:
                    currentRow.append(lastRow[index-1]+lastRow[index])
                    
            result.append(currentRow)
            
    return result