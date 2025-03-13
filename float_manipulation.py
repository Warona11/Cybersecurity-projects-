# Practical Task 1: Float Manipulation
import math

# Step 1: Ask the user to input 10 float numbers
numbers = []
print("Enter 10 numbers (floats or whole numbers):")
for i in range(10):
    while True:
        try:
            num = float(input(f"Enter number {i + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Step 2: Calculate and print the total of all numbers
total = sum(numbers)
print(f"The total of all numbers: {total}")

# Step 3: Find and print the index of the maximum value
max_index = numbers.index(max(numbers))
print(f"The index of the maximum value: {max_index}")

# Step 4: Find and print the index of the minimum value
min_index = numbers.index(min(numbers))
print(f"The index of the minimum value: {min_index}")

# Step 5: Calculate and print the average (rounded to 2 decimal places)
average = round(total / len(numbers), 2)
print(f"The average of the numbers: {average}")

# Step 6: Find and print the median
sorted_numbers = sorted(numbers)
if len(sorted_numbers) % 2 == 0:
    median = (sorted_numbers[4] + sorted_numbers[5]) / 2
else:
    median = sorted_numbers[len(sorted_numbers) // 2]
print(f"The median number: {median}")

# --- End of Practical Task 1 ---

