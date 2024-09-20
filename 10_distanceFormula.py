# 10. Write a program to read the values of two points on x-y plane and find out the distance between two points. Use math functions (sqrt, pow).



import math

x1=int(input("Enter the value of x1: "))
y1=int(input("Enter the value of y1: "))
x2=int(input("Enter the value of x2: "))
y2=int(input("Enter the value of y2: "))

dis=math.sqrt(pow((x1-x2),2) + pow((y1-y2),2))

print(f"The distance between points ({x1},{y1})  and ({x2},{y2}) :   {dis}")