'''
Merge Lists to Dictionary

Design a Python function named merge_lists_to_dictionary to merge two lists into a dictionary where elements from the first list act as keys and elements from the second list act as values.

Parameters:

keys (List): A list of keys.

values (List): A list of values.

Returns:

A dictionary containing merged key-value pairs.

Example:

Input: keys = ['a', 'b', 'c'], values = [1, 2, 3]
Output: {'a': 1, 'b': 2, 'c': 3}

Input: keys = ['x', 'y', 'z'], values = [10, 20, 30]
Output: {'x': 10, 'y': 20, 'z': 30}

'''

def merge_lists_to_dictionary(keys, values):
    # Your code goes here
    '''
    # Approach 1
    
    if len(keys) != len(values):
        return False 
        
    merged_dict = dict()
    
    for index in range(len(keys)):
        merged_dict[keys[index]] = values[index]
        
    return merged_dict
    '''
    
    # Approach 2
    if len(keys) != len(values):
        return False
        
    merged_dict = dict()
    
    for key, val in zip(keys, values):
        merged_dict[key] = val 
        
    return merged_dict
        