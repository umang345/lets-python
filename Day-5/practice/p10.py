def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    # Your code here
    
    result = list()
    
    currentNum = 0
    
    for rowIndex in range(1, n+1):
        row = list()
        
        numbersAdded = 0;
        while(numbersAdded<rowIndex):
            numbersAdded+=1
            currentNum+=1
            row.append(str(currentNum))
            if(numbersAdded!=rowIndex):
                row.append(" ")
                
        result.append("".join(row))
        
    return result
        
        
        
