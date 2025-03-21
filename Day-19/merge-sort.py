def merge_sort(arr):
    """
    Function to perform merge sort on a list of integers using recursion.
    
    Parameters:
    arr (list of int): The list to be sorted.
    
    Returns:
    list of int: The sorted list.
    """
    # Your code here
    merge_sort_helper(arr,0, len(arr)-1)
    return arr

def merge_sort_helper(arr, start, end):
    
    if start>=end:
        return 
    
    mid_index = start + (end-start)//2 
    
    merge_sort_helper(arr,start, mid_index)
    merge_sort_helper(arr, mid_index+1, end)
    __merge(arr, start, mid_index, end)
    
def __merge(arr, start, mid, end):
    
    i=start;j=mid+1
    current_merge_index = start
    merged_arr = list()
    
    while i<=mid and j<=end:
        
        if arr[i]<=arr[j]:
            merged_arr.append(arr[i])
            i+=1 
        else:
            merged_arr.append(arr[j])
            j+=1 
            
    while (i<=mid):
        merged_arr.append(arr[i])
        i+=1 
    while j<=end:
        merged_arr.append(arr[j])
        j+=1 
        
    for index in range(len(merged_arr)):
        arr[current_merge_index] = merged_arr[index]
        current_merge_index+=1 
        