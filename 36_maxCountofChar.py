# 36. Write a python program to find character having maximum count in a line of text


# Input: Take the string from the user
text = input("Enter a line of text: ")

# Create a dictionary to store character frequencies
char_count = {}

# Loop through each character in the string
for char in text:
    # Ignore spaces (optional, remove if you want to include spaces)
    if char != ' ':
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        else:
            # If the character is not in the dictionary, add it with a count of 1
            char_count[char] = 1

# Find the character with the maximum count
max_char = max(char_count, key=char_count.get)  # Get the character with the highest count
max_count = char_count[max_char]  # Get the count of that character

# Output the result
print(f"\nCharacter with maximum count: '{max_char}' appears {max_count} times.")
