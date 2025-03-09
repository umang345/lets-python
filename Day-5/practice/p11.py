

def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    # Your code here

    result = list()
    
    ## Upper triange
    for rowIndex in range(n):
        row = list()
        blankCount = n-rowIndex-1
        starCount = 2*(rowIndex+1)-1
        
        for blankIndex in range(blankCount):
            row.append(" ")
        for starIndex in range(starCount):
            row.append("*")
        for blankIndex in range(blankCount):
            row.append(" ")
            
        result.append("".join(row))
        
    
    ## Lower triange
    for rowIndex in range(n-1):
        row = list()
        blankCount = rowIndex+1 
        starCount = 2*(n-rowIndex-1)-1 
        
        for blankIndex in range(blankCount):
            row.append(" ")
        for starIndex in range(starCount):
            row.append("*")
        for blankIndex in range(blankCount):
            row.append(" ")
            
        result.append("".join(row))
        
    return result