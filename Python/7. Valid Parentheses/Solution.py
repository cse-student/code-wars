def valid_parentheses(string):
    if (string.count('(') != string.count(')')):
        return False
    
    count = 0
    for c in string:
        if c == '(':
             count = count + 1
        if c == ')':
            count = count -1
            if count < 0:
                return False
    return count == 0
