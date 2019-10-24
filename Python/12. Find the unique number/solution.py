def find_uniq(arr):
    lst = []
    s = set([])
    count = len(arr)
    for i in range(0, count):
        val = arr[i]
        if (val in lst):
            lst.remove(val)
            s.add(arr[i])
        if (val in s):
            continue
        lst.append(val)
    return lst[0]
