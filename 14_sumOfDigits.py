# 14. Write a Python function to calculate the sum of digits of a given integer.

def sum_of_digits(n):
    
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10  
        n //= 10         
    return total


num = int(input("Enter an integer: "))


print(f"The sum of digits of {num} is: {sum_of_digits(num)}")
