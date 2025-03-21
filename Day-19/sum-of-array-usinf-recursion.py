def sumArray(l1):
    if len(l1)==0:
        return 0
    if len(l1)==1:
        return l1[0]
    return l1[0]+sumArray(l1[1:])


print(sumArray([1,2,3,4,57]))