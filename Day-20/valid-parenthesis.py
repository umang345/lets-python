def is_balanced(S):
    
    brace_keys = {"(":")","{":"}","[":"]"}
    
    stack = []
    
    for brace in S:
        if brace in brace_keys.keys():
            stack.append(brace)
        else:
            if stack[-1] != brace_keys[brace]:
                return False
            
            stack.pop()
            
    return len(stack)==0


s = "{}{}"

print(is_balanced(s))