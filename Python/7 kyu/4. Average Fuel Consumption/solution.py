def solve(before, after):
    nd = after[1] - before[1] #new distance
    result = ((after[1]*after[0]) - (before[1]*before[0])) / nd
    return round(result, 1)