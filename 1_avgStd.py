# 1. Write a program to read five real numbers from user and find the average and standard deviation.


import math

numbers=[]

for i in range(5):
    num=int(input(f"Enter the {i+1} number: "))
    numbers.append(num)

s=sum(numbers)
avg=s/5
variance=sum((x-avg)**2 for x in numbers) /5
stddev=math.sqrt(variance)

print(numbers)
print("The sum: ", s)
print("The average: ",avg)
print("The variance: ",variance)
print("The standard deviation: ",stddev)

