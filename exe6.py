def find_number(numbers,target):
    if len(numbers) == 0:
        return -1
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return -1        
print(find_number([10, 20, 30, 40], 30))
print(find_number([10, 20, 30, 40], 99))
print(find_number([], 5))    