def count_smileys(arr):
    valid_eyes = [":", ";"]
    valid_noses = ["", "-", "~"]
    valid_mouths = [")", "D"]
    count = 0
    for i in arr:
        if (len(i) !=3 and len(i) != 2):
            continue
        if (len(i) == 3):
            if (i[0] in valid_eyes and i[1] in valid_noses and i[2] in valid_mouths):
                count += 1
        if (len(i) == 2):
            if (i[0] in valid_eyes and i[1] in valid_mouths):
                count += 1
    return count