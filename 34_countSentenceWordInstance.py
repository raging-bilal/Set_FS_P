# 34. Write a program in python to count number of sentences, no. of words and the word having maximum instance.


string=input("Enter the String to count the number of words: ")

len_count=[]


words=string.split()
count_w=len(words)
print(words)

sentence=string.split(".")
print(sentence)
count_s=len(sentence)


for i in words(len(words)):
    len_count.append(i)

print(len_count)

print("The number of words in the String: ",count_w)
print("The number of sentences in the String: ",count_s-1)














# Input: Take the string from the user
string = input("Enter a string: ")

# Step 1: Count the number of words
words = string.lower().split()  # Convert to lowercase and split the string into words
count_w = len(words)  # Number of words

# Step 2: Count the number of sentences
# We assume a sentence ends with '.', '!', or '?'
sentences = string.split('.') + string.split('!') + string.split('?')
sentences = [s.strip() for s in sentences if s.strip()]  # Remove empty strings and strip spaces
count_s = len(sentences)  # Number of sentences

# Step 3: Find the word with the maximum occurrence
word_count = {}  # Dictionary to store word occurrences
for word in words:
    word = word.strip('.,!?')  # Remove punctuation from words
    if word in word_count:
        word_count[word] += 1  # Increase the count if word exists in the dictionary
    else:
        word_count[word] = 1  # Add new word to the dictionary

# Find the word with the maximum occurrence
max_word = max(word_count, key=word_count.get)  # Get the word with the highest count
max_count = word_count[max_word]  # Get the count of that word

# Output the results
print("\nResults:")
print(f"The number of words: {count_w}")
print(f"The number of sentences: {count_s}")
print(f"The word with the maximum occurrence is '{max_word}' which appears {max_count} times.")
