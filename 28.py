# 28. Write programs in python to find element occurring odd number of times in a list.


# Define the list
my_list = [1, 2, 3, 2, 4, 3, 1, 5, 1, 3,99,99,99,100,100]

# Create a dictionary to count occurrences
count_dict = {}

# Count occurrences of each element
for element in my_list:
    count_dict[element] = count_dict.get(element, 0) + 1

# Find elements that occur an odd number of times
odd_occurrences = [element for element, count in count_dict.items() if count % 2 != 0]

# Print the results
print("Elements occurring an odd number of times:", odd_occurrences)
