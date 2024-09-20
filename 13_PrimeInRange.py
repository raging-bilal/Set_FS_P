# 13. Write a program to find prime numbers between two numbers


# Function to find prime numbers between two numbers
import math

def find_primes(a, b):
    # Loop through each number in the range
    for i in range(a, b + 1):
        if i > 1:  # Prime numbers are greater than 1
            is_prime = True
            # Check divisibility from 2 to sqrt(i)
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                print(i,end=" ")

# Input: range of numbers
a = int(input("Enter the initial range: "))
b = int(input("Enter the final range: "))

# Call the function
find_primes(a, b)


