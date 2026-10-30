def first_duplicate(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return number
        seen.add(number)
    return None
print(first_duplicate([2, 5, 3, 5, 2]))
print(first_duplicate([1, 2, 3, 4]))
print(first_duplicate([7, 7, 8]))          
