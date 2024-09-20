# 23. Write programs in python WAP to merge Two Lists and Sort it.



# l1=[12,34,67,98,43]
# l2=[23,56,78,55,42]

# l=l1+l2

# print(l)

# l.sort()

# print("Final List: ",l)

lst=[]
n=int(input("Enter ho many elements you want to enter in the list: "))

for i in range(n):
    new=int(input("Enter the element of list: "))
    lst.append(new)


print("The final list as given by user: ", lst)