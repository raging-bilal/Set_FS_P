# 35. Write a python program to count frequency of each character in a line of text.



# Input: Take the string from the user
text = input("Enter a line of text: ")

# Create a dictionary to store character frequencies
char_count = {}

# Loop through each character in the string
for char in text:
    # Ignore spaces (optional, remove if you want to count spaces)
    if char != ' ':
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        else:
            # If the character is not in the dictionary, add it with a count of 1
            char_count[char] = 1

# Output the results
print("\nCharacter Frequency:")
for char, count in char_count.items():
    print(f"'{char}': {count}")
