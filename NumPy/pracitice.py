import numpy as np
# =================================================
list = [1,2,3,4,5,6,7,8,9]
arr = np.array(list)
print(arr)
print ("Sum: ",np.sum(arr))
print("max: ",np.max(arr))
print("min",np.min(arr))
print("mean: ",np.mean(arr))
print("std: ",np.std(arr))
# ====================================
arr1=np.arange(1,10)
arr1=arr1.reshape(3,3)
second_row =arr1[1,:]
third_colomn=arr1[:,2]
print(arr1)
print("Second row ",second_row)
print("third colomn: ",third_colomn)