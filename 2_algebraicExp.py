# 2. Write a program to compute the value of the following algebraic expression. The value of x and y will be read using input() function.

x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))

result= (  1+ (x/y)+ (x**y )  )   /    (  2 + (y/x)+ (y**x )  )

print("The result of the expression: ",result)