def Descending_Order(num):
    lst = list(str(num))
    lst.sort(reverse=True)
    return int(''.join(lst))