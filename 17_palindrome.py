# 17. Write Python Program to Check Whether a String is Palindrome or Not

s=input("Enter the string to check for palindrome: ")

s=s.replace(" ","")

s=s.lower()

rev=s[::-1]

print("The original string: ",s)
print("The reversed string: ",rev)

if(s==rev):
    print(f"{s} is palindrome!")

else:
    print(f"{s} is NOT palindrome!")