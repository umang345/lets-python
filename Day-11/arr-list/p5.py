'''
Description:
Given a list of integers and an integer D, write a function to rotate the list to the left by D positions.



Input Parameters:

ARR (List[int]): A list of integers.

D (int): The number of positions to rotate the list to the left.

Output:

List[int]: The list after rotating it to the left by D positions.



Example:

Input: ARR = [1, 2, 3, 4, 5], D = 2
Output: [3, 4, 5, 1, 2]
 
Input: ARR = [10, 20, 30, 40, 50], D = 3
Output: [40, 50, 10, 20, 30]
 
Input: ARR = [7, 8, 9, 10], D = 1
Output: [8, 9, 10, 7]
'''

def reverseList(arr, start, end):
    
    while(start<=end):
        tmp = arr[start]
        arr[start] = arr[end]
        arr[end] = tmp 
        start+=1 
        end -=1
        
    return arr

def rotate_left(arr, d):
    """
    Function to rotate the list to the left by D positions.
    :param ARR: List[int] -> The list of integers
    :param D: int -> The number of positions to rotate
    :return: List[int] -> The list after rotation
    """
    
    ###  Approach 1  ###
    
    # k=0
    # rotated = list()
    # d = d%(len(arr))
        
    
    # for index in range(d,len(arr)):
    #     rotated.append(arr[index])
        
    # for index in range(0,d):
    #     rotated.append(arr[index])
        
    # return rotated
    
    
    ### Approach 2 ###
    
    # Reverse first D elements
    
    d = d%(len(arr))
    arr = reverseList(arr, 0, d-1)
    arr = reverseList(arr, d, len(arr)-1)
    arr = reverseList(arr, 0 , len(arr)-1)
    
    return arr