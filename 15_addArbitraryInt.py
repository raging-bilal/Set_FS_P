# 15. Write a function to add arbitrary integers.


# Function to sum arbitrary integers
def sum_arbitrary_integers(*args):
    return sum(args)

# Input: arbitrary integers (comma-separated)
nums = list(map(int, input("Enter integers separated by spaces: ").split()))

# Call the function and print the result
print(f"The sum of the integers is: {sum_arbitrary_integers(*nums)}")
