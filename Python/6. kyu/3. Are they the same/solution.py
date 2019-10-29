def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    if (len(array1) != len(array2)):
        return False
    array3 = []
    for i in array1:
        array3.append(i**2)
    for i in array3:
        if i in array2:
            array2.remove(i)
    return len(array2) == 0
