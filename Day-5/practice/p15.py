def generate_hollow_inverted_right_angled_triangle(n):
    """
    Function to return a hollow inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    
    result = list()
    
    if n==0:
        return list
        
    row = []
    for columnIndex in range(n):
        row.append("*")
    result.append("".join(row))
    
    if n>2:
        
        for rowIndex in range(n-2, 0,-1):
            row = []
            row.append("*")
            blackCount = rowIndex-1
            for blankIndex in range(blackCount):
                row.append(" ")
            row.append("*")
            result.append("".join(row))
    
    if n>1:
        result.append("*")
        
    return result
    