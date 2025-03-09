def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    # Your code here

    result = []
    
    for rowIndex in range(1,n+1):
        row = list()
        oneSideSpaceCount = n - rowIndex
        starCount = (2*rowIndex)-1
        
        for blankIndex in range(1,oneSideSpaceCount+1):
            row.append(" ")
        for starIndex in range(1,starCount+1):
            row.append("*")
        for blankIndex in range(1, oneSideSpaceCount+1):
            row.append(" ")
        
        result.append("".join(row))
    
    return result
        