def binary_search(arr, target):
    start = 0
    end = len(arr)-1

    while start<=end:
        mid = start + ((end-start)//2)
        if arr[mid] == target:
            return mid 
        if arr[mid]>target:
            end = mid-1
        else:
            start=mid+1

    return -1 

sorted_list = [10,20,30,40,50,60,70,86]
target = 50

result = binary_search(sorted_list, target)
print(result)