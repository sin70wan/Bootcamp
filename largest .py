def find_largest(numbers):
    if len(numbers) == 0:
        return None

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


user_input = input("Enter numbers separated by space: ")
numbers = list(map(int, user_input.split()))

result = find_largest(numbers)

print("Largest number is:", result)