def generate_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    
    triange = list()
    
    for rowIndex in range(1, n+1):
        row = list()
        for columnIndex in range(1, rowIndex+1):
            row.append("*")
            
        triange.append("".join(row))
        

    return triange