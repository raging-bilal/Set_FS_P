# 41. Write a python program to find the average value of the second column of a 2D numpy array.

import numpy as np

array_2D=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])


print(array_2D)

c2=array_2D[:,1]
print("C2: ",c2)

mean_c2=np.mean(c2)

print("The mean of c2: ",mean_c2)
