# 18. Write a Python program that first accept a string and If the string length is less than 4, return empty string. Then create a string made of the first 2 and the last 2 chars from the accepted string. 
# Sample String : ‘New Delhi'
# Expected Result : ‘Nehi'
# Sample String : ‘New'
# Expected Result : Empt String
# Sample String : ' w'
# Expected Result : Empty String


s=input("Enter the string: ")

print("Sample String : ",s)

l=len(s)

if l<4:
    print("INVALID INPUT! ")

else:
    s1=s[:2]
    s2=s[l-2:]

    res=s1+s2

    print("Expected Result: ",res)