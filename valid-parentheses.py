def valid_parentheses(string):
    open_parentheses = 0
    for char in string:
        if char == '(': open_parentheses += 1
        if char == ')': open_parentheses -= 1
        if open_parentheses < 0: return False 
    return True if open_parentheses == 0 else False
