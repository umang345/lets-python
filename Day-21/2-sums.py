def two_sum(nums, target):
    """
    Function to return indices of the two numbers such that they add up to the target.
    
    :param nums: List[int] -> The input list of integers
    :param target: int -> The target sum
    :return: List[int] -> A list of two indices whose corresponding elements add up to the target
    """
    
    hashmap = {}
    result = None
    
    for index in range(len(nums)):
        hashmap[nums[index]] = index
        
    for index in range(len(nums)):
        
        
        del hashmap[nums[index]]
            
        curr_target = target - nums[index]
        
        if not hashmap.get(curr_target) is None:
            result = sorted([index, hashmap.get(curr_target)])
            
        hashmap[nums[index]] = index
        
    
    return result   


nums = [2, 7, 11, 15]; target = 9

print(two_sum(nums,target))