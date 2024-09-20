# 45. Write a python program to find the maximum of average value in each row of a 2D numpy array.

import numpy as np

array_2D=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19,20]
])

print(array_2D)


avg=np.mean(array_2D,axis=1)
print("The avg: ",avg)

maximum=np.max(avg)
print("The maximum of average: ",maximum)

