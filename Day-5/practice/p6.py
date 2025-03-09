def generate_inverted_triangle(n):
    """
    Function to return an inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here

    result = list()
    
    for rowIndex in range(n,0,-1):
        row = list()
        for columnIndex in range(1, rowIndex+1):
            row.append("*")
        result.append("".join(row))
    
    return result