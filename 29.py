# 29. Read a List of Words and Return the Length of the Longest One


# Function to read a list of words and return the length of the longest one
def longest_word_length():
    # Read input from the user
    words = input("Enter a list of words separated by spaces: ").split()
    
    # Check if the list is empty
    if not words:
        return 0
    
    # Find the length of the longest word
    longest_length = max(len(word) for word in words)
    
    return longest_length

# Call the function and print the result
length_of_longest = longest_word_length()
print("The length of the longest word is:", length_of_longest)
