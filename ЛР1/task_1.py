numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

len_of_numbers = len(numbers)
sum_of_numbers = sum(numbers[:4]+numbers[5:])

middle_arithmetic = sum_of_numbers/len_of_numbers

numbers[4] = middle_arithmetic

print(numbers)
