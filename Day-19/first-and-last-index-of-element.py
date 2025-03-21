def firstIndexOfAnElement(l1,x):
    if len(l1)==0:
        return -1
    
    if l1[0]==x:
        return 0
    
    ans =  firstIndexOfAnElement(l1[1:],x)
    if ans!=-1:
        ans+=1

    return ans

print(firstIndexOfAnElement([3,2,5,2,8,2,1],2))
print(firstIndexOfAnElement([3,2,5,2,8,2,1],10))
print(firstIndexOfAnElement([3,2,5,2,8,2,1],1))
