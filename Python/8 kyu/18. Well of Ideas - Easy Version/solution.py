def well(x):
    c = x.count('good')
    if (c < 1):
        return 'Fail!'
    if (c < 3):
        return 'Publish!'
    return 'I smell a series!'