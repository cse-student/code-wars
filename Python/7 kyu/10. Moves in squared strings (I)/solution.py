def vert_mirror(strng):
	lst = strng.split('\n')
	return '\n'.join(lst[i][::-1] for i in range(len(lst)))

def hor_mirror(strng):
    lst = strng.split('\n')
    return '\n'.join(reversed(lst))

def oper(fct, s):
	return fct(s)