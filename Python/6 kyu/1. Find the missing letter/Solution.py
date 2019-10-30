def xo(s):
    x = 0
    o = 0
    for c in s:
        if c.lower() == 'x':
            x = x + 1
        elif c.lower() == 'o':
            o = o + 1
    return x == o