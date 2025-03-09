def generate_hollow_right_angled_triangle(n):
    """
    Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    
    result = list()
    
    if n==0:
        return result
        
    result.append("*")
    
    
    if n>2:
        for rowIndex in range(n-2):
            row = list()
            row.append("*")
            blankCount = rowIndex
            for blankIndex in range(blankCount):
                row.append(" ")
            row.append("*")
            
            result.append("".join(row))

    if n>1:
        row = list()
        for columnIndex in range(n):
            row.append("*")
        result.append("".join(row))
        
    return result