def generate_rectangle(n, m):
    """
    Function to return a rectangle pattern of '*' with length n and breadth m as a list of strings.
    
    Parameters:
    n (int): The number of rows in the rectangle.
    m (int): The number of columns in the rectangle.
    
    Returns:
    list: A list of strings where each string represents a row of the rectangle pattern.
    """
    # Your code here

    result = []
    
    for rowIndex in range(1,n+1):
        row = []
        for columnIndex in range(1, m+1):
            row.append("*")
        
        result.append("".join(row))
        
    return result