# 19. Write a Python program to delete ‘e’ from the end of a given string (length should be at least 3) and add ‘en' at the end. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : ‘Give'
# Expected Result : ‘Given'
# Sample String : ‘take'
# Expected Result : ‘taken’ 
# Sample String : ‘ta’ 
# Expected Result : ‘ta’



s=input("Enter the string: ")

print("Sample String : ",s)

l=len(s)

if l<3:
    print("Less than 3. So, Expected Result:  ", s)

else:
    if s[-1]=="e":
        s=s[:-1]+"en"
        print("Expected Result: ",s)


