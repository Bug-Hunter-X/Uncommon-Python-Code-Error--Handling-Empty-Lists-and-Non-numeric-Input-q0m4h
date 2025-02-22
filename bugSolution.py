def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        raise ValueError("Input list contains no numeric values.")
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

try:
    my_numbers = [10, 20, 30, 40, 50]
    average = calculate_average(my_numbers)
    print(f"The average is: {average}")

    my_numbers = []
    average = calculate_average(my_numbers)
    print(f"The average is: {average}")

    my_numbers = [10, 20, 30, 40, 50, 'a']
    average = calculate_average(my_numbers)
    print(f"The average is: {average}")
except ValueError as e:
    print(f"Error: {e}")
    