def generate_right_angled_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    
    result = list()
    
    for rowIndex in range(n):
        row = list()
        blankCount = n - rowIndex -1
        starCount = rowIndex + 1
        
        for blankIndex in range(blankCount):
            row.append(" ")
        for starIndex in range(starCount):
            row.append("*")
            
        result.append("".join(row))
        
    return result
