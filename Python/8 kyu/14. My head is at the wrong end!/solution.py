def fix_the_meerkat(arr):
    temp = arr[0]
    arr[0] = arr[2]
    arr[2] = temp
    return arr