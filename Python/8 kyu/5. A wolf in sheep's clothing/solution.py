def warn_the_sheep(queue):
    c = len(queue)
    if (queue[c-1] == 'wolf'):
        return "Pls go away and stop eating my sheep"
    pos = c - 1 - queue.index("wolf")
    return 'Oi! Sheep number ' + str(pos) + '! You are about to be eaten by a wolf!'