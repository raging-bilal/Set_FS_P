# 37. Write a program in python to check whether a sentence is pangram or not. A pangram, or holo-alphabetic sentence, is a sentence that contains every letter of the alphabet at least once.




# Function to check if the sentence is a pangram
def is_pangram(sentence):
    # Initialize an empty set to track unique letters
    letters = set()

    # Loop through each character in the sentence
    for char in sentence.lower():
        # If the character is a letter, add it to the set
        if char.isalpha():
            letters.add(char)

    # Check if we have all 26 letters
    return len(letters) == 26

# Input: Take the sentence from the user
sentence = input("Enter a sentence: ")

# Check if the sentence is a pangram
if is_pangram(sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is NOT a pangram.")

























# Function to check if the sentence is a pangram
def is_pangram(sentence):
    # Create a set of all 26 letters of the alphabet (ignoring case)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    
    # Convert the sentence to lowercase and create a set of characters in the sentence
    sentence_letters = set(sentence.lower())
    
    # Check if all alphabet letters are in the sentence set
    return alphabet.issubset(sentence_letters)

# Input: Take the sentence from the user
sentence = input("Enter a sentence: ")

# Check if the sentence is a pangram
if is_pangram(sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is NOT a pangram.")
