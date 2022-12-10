def find_max(numbers):
    max_number = 0
    for n in numbers:
        if n > numbers[0]:
            max_number = n
        else:
            max_number = numbers[0]
    return max_number
