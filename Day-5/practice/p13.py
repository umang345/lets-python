def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the sandglass.
    
    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.
    """
    # Your code here
    
    result = list()
    
    ## Upper inverted triangle
    for rowIndex in range(n):
        row = list()
        oneSidedBlankCount = rowIndex
        starCount = 2*(n-rowIndex)-1
        
        for blankIndex in range(oneSidedBlankCount):
            row.append(" ")
        for starCount in range(starCount):
            row.append("*")
        for blankCount in range(oneSidedBlankCount):
            row.append(" ")
            
        result.append("".join(row))
    
    
    ## Lower triangle
    for rowIndex in range(1,n):
        row = list()
        oneSidedBlankCount = n - rowIndex -1
        starCount = 2*(rowIndex+1)-1 
        
        for blankIndex in range(oneSidedBlankCount):
            row.append(" ")
        for starCount in range(starCount):
            row.append("*")
        for blankCount in range(oneSidedBlankCount):
            row.append(" ")
            
        result.append("".join(row))
        
    return result