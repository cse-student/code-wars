def add_letters(*letters):
    if (len(letters) == 0):
        return 'z'
    result = 96
    for i in letters:
        result += ord(i)
        result -= 96
        if result > 122:
            result -= 26
    return chr(result)