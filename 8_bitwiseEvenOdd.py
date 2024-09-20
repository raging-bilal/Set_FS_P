# 8. Write a program to read an integer and use bitwise operators to check the nature (even or odd) of the integer.
# ▪ Property: 
# ▪ The binary representation of every odd integer consists of 1 at the rightmost position. 
# ▪ The binary representation of every even integer consists of 0 at the rightmost position.



# Read an integer from the user
num = int(input("Enter an integer: "))

# Check if the number is even or odd using the bitwise AND operator
if num & 1 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
