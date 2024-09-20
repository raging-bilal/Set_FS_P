# 9. Write a program to find the maximum of three numbers.


a=int(input("Enter the value of a: "))

b=int(input("Enter the value of b: "))

c=int(input("Enter the value of c: "))


print("a: ",a)
print("b: ",b)
print("c: ",c)

# if(a>b and b>c):
#     print(f"{a} is maximum! ")

# elif(b>a and b>c):
#     print(f"{b} is maximum! ")

# else:
#     print(f"{c} is maximum! ")


res=max(a,b,c)
print("The maX: ",res)

