def longest(s1, s2):
    #merge 2 string
    #form a set using the output of the previous operation thus eliminating all duplicates
    #finally using the join method to rebuild the string using the formed set
    return ''.join(sorted(set(s1+ s2)))