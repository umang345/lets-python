def generate_number_triangle(n):
    """
    Function to return a right-angled triangle of repeated numbers of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here

    result = list()
    
    for rowIndex in range(1, n+1):
        row = list()
        for columnIndex in range(rowIndex):
            row.append(str(rowIndex))
        result.append("".join(row))
        
    return result
        