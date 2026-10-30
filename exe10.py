def move_zeros(numbers):
    result = []
    for number in numbers:
        if number != 0:
            result.append(number)
    result.extend([0]* numbers.count(0))
    return result

print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([1, 2, 3]))
print(move_zeros([0, 0, 0]))