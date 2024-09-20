# 24. Write programs in python to find the second largest number in a List and all its index.

# Initialize an empty list
lst = []
n = int(input("Enter the length of the list: "))

# Collect elements from the user
for i in range(n):
    elements = int(input("Enter the elements of the list one by one: "))
    lst.append(elements)

print("The final list:", lst)

# Use a set to find unique elements and then convert to a list
unique_lst = list(set(lst))

# Sort the unique list
unique_lst.sort()

# Check if there are at least two unique elements
if len(unique_lst) < 2:
    print("There are not enough unique elements to find the second largest.")
else:
    second_largest = unique_lst[-2]
    print("The second largest element is:", second_largest)

    # Find all indices of the second largest element in the original list
    indices = [i for i, x in enumerate(lst) if x == second_largest]
    print("Its index values are:", indices)


