def generate_inverted_pyramid(n):
    """
    Function to return an inverted pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the inverted pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the inverted pyramid.
    """
    # Your code here
    
    result = list()
    
    for rowIndex in range(n):
        
        row = list()
        oneSideSpaceCount = rowIndex
        starCount = 2*(n-rowIndex)-1
        
        for blankIndex in range(oneSideSpaceCount):
            row.append(" ")
        for startIndex in range(starCount):
            row.append("*")
        for blankIndex in range(oneSideSpaceCount):
            row.append(" ")
        
        result.append("".join(row))
        
    return result
