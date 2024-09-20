# 42. Write a python program to find the average value of the first 5 rows of the third and fourth columns of a 2D numpy array.

import numpy as np

array_2D=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19,20]
])

print(array_2D)


# the average value of the first 5 rows of the third columns

r5c3=array_2D[:5,2]
print("first 5 rows of the third columns: ",r5c3)

avg1=np.mean(r5c3)
print("The avg1: ",avg1)


# the average value of the first 5 rows of the fourth columns

r5c4=array_2D[:5,3]
print("first 5 rows of the forth columns: ",r5c4)

avg2=np.mean(r5c4)
print("The avg2: ",avg2)





