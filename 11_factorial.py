# 11. Write a program to compute the factorial of an integer


# n=int(input("Enter the positive integer to check for the factorial: "))
# fact=1
# for i in range(1,n+1):
#     fact=fact * i


# print(f"The factorial of {n} is {fact} !")




# Using Recursion also-------------------------


def fac(n):
    if (n==0 or n==1):
        return 1
    else:
        return n* fac(n-1)
    

n=int(input("Enter the positive integer to check for the factorial using recursion: "))
if n<0:
    print("Invalid input! Please enter positive integers!")

else:
    print(f"The factorial of {n} is {fac(n)} !")
