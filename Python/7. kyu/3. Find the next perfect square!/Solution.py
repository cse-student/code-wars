def find_next_square(sq):
    root = sq ** 0.5
    if (root == int(root)):
        return (root+1)**2
    else:
        return -1