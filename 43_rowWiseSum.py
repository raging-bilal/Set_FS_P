# 43. Write a python program to compute the row wise sum of all possible values in a 2D numpy array.


import numpy as np

array_2D=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19,20]
])

print(array_2D)


sum=np.sum(array_2D,axis=1)
print(sum)





# sum1=np.sum(array_2D[0,:])
# sum2=np.sum(array_2D[1,:])
# sum3=np.sum(array_2D[2,:])
# sum4=np.sum(array_2D[3,:])
# sum5=np.sum(array_2D[4,:])

# print(f"{sum1} {sum2} {sum3} {sum4} {sum5} ")


