def sum_two_smallest_numbers(numbers):
    num1 = -1 
    while (num1 < 0):
        num1 = min(numbers)
        numbers.remove(num1)
    return num1 + min(numbers)