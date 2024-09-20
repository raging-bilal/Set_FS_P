# 22. Write programs in python for the following: Read a list and transfer even and odd integers into Two Different Lists.


# l=[23,445,3,33,22,3,55,6,6,56,5,4,32333,23,22234,5,6543,322]
# e=[]
# o=[]

# for i in l:
#     if i%2==0:
#         e.append(i)

#     else:
#         o.append(i)

# print("Original List: ",l)
# print("Odd Numbers List:" ,o)
# print("Even Numbers List:" ,e)





l = [23, 445, 3, 33, 22, 3, 55, 6, 6, 56, 5, 4, 32333, 23, 22234, 5, 6543, 322]
e = []
o = []

for i in l:
    if isinstance(i, int):  # Check if the element is an integer
        if i % 2 == 0:
            e.append(i)
        else:
            o.append(i)
    else:
        print(f"Warning: {i} is not an integer and will be skipped.")

print("Original List:", l)
print("Odd Numbers List:", o)
print("Even Numbers List:", e)
