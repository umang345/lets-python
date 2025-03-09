def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.
    
    Parameters:
    n (int): The height of the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.
    """
    # Your code here

    result = list()
    
    for rowIndex in range(1, n+1):
        row = list()
        leadingBlankCount = n-rowIndex
        currentNum = 1;
        
        for blankIndex in range(leadingBlankCount):
            row.append(" ")
        
        while(currentNum<=rowIndex):
            row.append(str(currentNum))
            if currentNum!=rowIndex:
                row.append(" ")
            currentNum+=1 
            
        for blankIndex in range(leadingBlankCount):
            row.append(" ")
            
        result.append("".join(row))
        
    return result
        