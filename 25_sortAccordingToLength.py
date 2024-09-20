# 25. Write programs in python to sort a List according to the length of the elements.


# Define a list of strings
my_list = ["apple", "banana", "pear", "kiwi", "grapefruit", "fig"]

# Sort the list by the length of each element
sorted_list = sorted(my_list, key=len)

# Print the sorted list
print("Original List:", my_list)
print("Sorted List by Length:", sorted_list)
