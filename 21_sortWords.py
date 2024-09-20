# 21. Write Python Program to Sort Words in Alphabetic Order.


def sort_words_alphabetically(input_string):
    # Split the string into words
    words = input_string.split()
    # Sort the words in alphabetical order
    words.sort()
    return words

# Example usage
input_string = input("Enter a string: ")
sorted_words = sort_words_alphabetically(input_string)

print("Words in Alphabetic Order:", sorted_words)
