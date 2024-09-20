# 40. Write a python program to count number of lines, words, characters, alphabets and digits in file.


# Function to count lines, words, characters, alphabets, and digits in a file
def file_statistics(filename):
    lines_count = 0
    words_count = 0
    characters_count = 0
    alphabets_count = 0
    digits_count = 0

    with open(filename, 'r') as file:
        for line in file:
            lines_count += 1
            words_count += len(line.split())
            characters_count += len(line)
            
            # Count alphabets and digits in the line
            for char in line:
                if char.isalpha():
                    alphabets_count += 1
                elif char.isdigit():
                    digits_count += 1

    return lines_count, words_count, characters_count, alphabets_count, digits_count

# Input: Get the file name from the user
filename = input("Enter the file name: ")

try:
    # Get the statistics from the file
    lines, words, characters, alphabets, digits = file_statistics(filename)
    
    # Output the results
    print(f"Number of lines: {lines}")
    print(f"Number of words: {words}")
    print(f"Number of characters: {characters}")
    print(f"Number of alphabets: {alphabets}")
    print(f"Number of digits: {digits}")

except FileNotFoundError:
    print(f"File '{filename}' not found.")
