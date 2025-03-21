def quick_sort(arr):
    """
    Function to perform quick sort on a list of integers using recursion.
    
    Parameters:
    arr (list of int): The list to be sorted.
    
    Returns:
    list of int: The sorted list.
    """
    # Your code here
    quick_sort_helper(arr, 0, len(arr)-1)
    return arr
    
    
def quick_sort_helper(arr, start, end):
    if start>=end:
        return 
    
    pivot_index = __partition(arr, start, end)
    
    quick_sort_helper(arr, start, pivot_index-1)
    quick_sort_helper(arr, pivot_index+1, end)
    
    
def __partition(arr, start, end):
    
    # print(f"Partition : {start}-{end} ")
    pivot = arr[end]
    
    currentIndex = start 
    
    for index in range(start, end+1):
        if arr[index]<pivot:
            currentIndex += 1

    

    arr[currentIndex], arr[end] = arr[end], arr[currentIndex]
    

    
    i = start; j = currentIndex+1 
    
    while i<currentIndex and j<=end:
        if arr[i]>arr[currentIndex]:
            arr[i], arr[j] = arr[j],arr[i]
            j+=1 
        i+=1

    i = start; j = currentIndex+1
    while i<currentIndex and j<=end:
        if arr[j]<arr[currentIndex]:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
        j+=1  
        
    print(f"Partition : {start}-{end} => {currentIndex}  =>  {arr}")
    return currentIndex
    
    
arr = [3, 0, 2, 5, -1, 4, 1]
print(quick_sort(arr))  
    
    
    
    
    
    
    
    
    
    
    
    
    
