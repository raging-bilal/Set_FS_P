# 26. Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number.

# Define the range of numbers
n = int(input("Enter the range of numbers (0 to n): "))

# Create a list of tuples (number, square of number)
list_of_tuples = [(i, i**2) for i in range(n + 1)]

# Print the resulting list of tuples
print("List of tuples (number, square):", list_of_tuples)
