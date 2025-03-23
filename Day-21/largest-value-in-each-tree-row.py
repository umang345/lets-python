from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def largest_values_in_rows(root):
    """
    Find the largest value in each row of an N-ary tree.

    Parameters:
    root (Node): The root of the N-ary tree.

    Returns:
    List[int]: A list of integers where each integer is the largest value in that level of the tree.
    """
    freq = {}
    largest_values_in_rows_helper(root, freq)
    
    result = [ freq[key] for key in sorted(freq.keys())]
    return result

def largest_values_in_rows_helper(root:Node, freq:dict, level:int=0):
    
    if root is None:
        return 
    
    if freq.get(level) is None:
        freq[level] = root.val 
    else:
        if freq[level]<root.val:
            freq[level] = root.val 
            
    
    for child in root.children:
        largest_values_in_rows_helper(child, freq, level+1)


root = Node(1, [
    Node(3, [Node(5), Node(6)]),
    Node(2),
    Node(4)
])

print(largest_values_in_rows(root))