# 39. Write a program to read a string and find numbers of digits and alphabets.


# Function to count digits and alphabets in a string
def count_digits_and_alphabets(string):
    digits_count = 0
    alphabets_count = 0

    # Loop through each character in the string
    for char in string:
        if char.isdigit():  # Check if character is a digit
            digits_count += 1
        elif char.isalpha():  # Check if character is an alphabet
            alphabets_count += 1

    return digits_count, alphabets_count

# Input: Take the string from the user
input_string = input("Enter a string: ")

# Call the function and get the count of digits and alphabets
digits, alphabets = count_digits_and_alphabets(input_string)

# Output the results
print(f"Number of digits in the string: {digits}")
print(f"Number of alphabets in the string: {alphabets}")
