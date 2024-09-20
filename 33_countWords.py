# 33. Write a program in python to count the words in a line of text.



string=input("Enter the String to count the number of words: ")

words=string.split()

count=len(words)

print("The number of words in the String: ",count)