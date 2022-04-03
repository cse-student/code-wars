def pattern(n):
    if n == 0 or n == None:
        return ""
    result = ""
    for i in range(1,n+1):
        if i != 1:
            result += '\n'
        for j in range(i, n+1):
            result += str(j)
        for j in range(1, i):
            result += str(j)
    return result
    