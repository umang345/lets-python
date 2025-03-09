def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    
    ## Add line  1 
    ## Add n-2 lines
    ## Add last line 
    
    result = []
    
    if (n>0):
        row = []
        for i in range(n):
            row.append("*")
        result.append("".join(row))
        
    if (n>2):
        for rowIndex in range(1,n-1):
            row = []
            row.append("*")
            for columnIndex in range(1,n-1):
                row.append(" ");
            row.append("*")
            result.append("".join(row))
    
    if (n>1):
        row = []
        for i in range(n):
            row.append("*")