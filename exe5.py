def count_occurance(numbers,target):
    count = 0
    for number in numbers:
        if number == target:
           count += 1
    return count

print(count_occurance([2, 4, 2, 7, 2], 2))
print(count_occurance([1, 3, 5], 2))
print(count_occurance([], 4))