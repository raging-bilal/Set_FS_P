# 5. Write a program to read the values of two integer variables and use bitwise operators to exchange the values of the variables (^ operator).

num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))

print("Num1: ",num1)
print("Num2: ",num2)

num1=num1^num2
num2=num1^num2
num1=num1^num2

print("After Swapping ")
print("Num1: ",num1)
print("Num2: ",num2)




