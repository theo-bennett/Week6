def find_first_even_number(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
    else:
        return None

result = find_first_even_number([1, 3, 5, 6, 7, 8])
print(result) 


# the reason why it was displaying none was bcs it was indented wrong 