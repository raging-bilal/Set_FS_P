# 32. Write a Python program to remove an empty tuple(s) from a list of tuples.


# Original list with some empty tuples
list_of_tuples = [(), (1, 2), (), (3, 4), (), (5,), (), (6, 7)]

# Create a new list to store non-empty tuples
result = []

# Loop through each tuple in the original list
for tup in list_of_tuples:
    # If the tuple is not empty, add it to the result list
    if tup:
        result.append(tup)

# Print the list after removing empty tuples
print("List after removing empty tuples:", result)
