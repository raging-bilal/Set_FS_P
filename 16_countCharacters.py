# 16. Write a function to receive multiple strings and count total characters. 


# Function to count total characters in multiple strings
def count_total_characters(*args):
    total_characters = 0
    for string in args:
        total_characters += len(string)
    return total_characters

# Input: multiple strings (comma-separated)
strings = input("Enter multiple strings separated by commas: ").split(',')

# Call the function and print the result
print(f"The total number of characters is: {count_total_characters(*strings)}")
