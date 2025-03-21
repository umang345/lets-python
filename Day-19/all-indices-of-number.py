def printAllIndicesOfAnArray(arr, element):
    printAllIndicesOfArrayHelper(arr, element)

def printAllIndicesOfArrayHelper(arr, element, index=0):
    if index >= len(arr):
        return

    if len(arr)==0:
        print("-1")

    if arr[index]==element:
        print(index)

    printAllIndicesOfArrayHelper(arr, element, index+1)
 


printAllIndicesOfAnArray([3,2,5,2,8,2,1],2)