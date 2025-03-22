import math

def evaluate_postfix(expression):
    """
    Function to evaluate a postfix expression.
    :param expression: List[str] -> A list of strings representing the postfix expression
    :return: int -> The result of the postfix evaluation
    """
    # TODO: Implement this function
    
    ops = {
        "+": lambda x,y:x+y,
        "-": lambda x,y:x-y,
        "*": lambda x,y:x*y,
        "/": lambda x,y:math.trunc(x/y)
    }
    
    stack = list()
    
    for s in expression:
        print(stack)
        if not s in ops.keys():
            stack.append(int(s))
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(ops[s](operand2, operand1))
            
    return stack[-1]


print(evaluate_postfix(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))