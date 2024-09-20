# 12. Write a program to check whether the integer is prime.

n=int(input("Enter the positive integer to check for the prime: "))

if n<=1:
    print("Not Prime")

else:

    for i in range(2,n):
        if n%i==0:
            print("Not Prime!") 
            break

    else:
        print("Prime!")

