# 30. Write a Python program to find the repeated items of a tuple. 


# Define a tuple
my_tuple = (1, 2, 3, 2, 4, 5, 1, 6, 3, 1)

# Create a dictionary to count occurrences
count_dict = {}

# Count occurrences of each element
for item in my_tuple:
    count_dict[item] = count_dict.get(item, 0) + 1

# Find repeated items (those with a count greater than 1)
repeated_items = [item for item, count in count_dict.items() if count > 1]

# Print the results
print("Repeated items in the tuple:", repeated_items)
