def checkSorted(l1):
    if len(l1)==0 or len(l1)==1:
        return True 

    ans = checkSorted(l1[1:])
    return ans and (l1[0] < l1[1])

print(checkSorted([2,5,6,8,9]))
print(checkSorted([2,5,8,9,2]))