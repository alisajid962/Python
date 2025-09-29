import numpy as np

arr = np.arange(1,16)

print(arr)
print(arr[0:10])
# broadcasting its channge the original unitle you copy it then broadcast it 
arr[5:]=100
print(arr)
# print(arr.reshape(3,5))
arr1=np.arange(1,51).reshape(5,10)
print(arr1)
print(arr1[3:,6:8])
print("Ind,",arr1[0:5])
arr1[2][5]
# print(type(arr1))
arr1[0:2,4:6]
list1 = [1,2,3,4,5,6,7,8,9]
arli=np.array(list1)

invalid = arli<4
broadcasting_copy =arli.copy()
broadcasting_copy[0:3]=100

unvalid=arli[invalid].copy()
print(arli)
print(unvalid)
print(broadcasting_copy)
print("operations * : ",arli*3)
print("Sqrt of all elements: ",np.sqrt(arli))
print("Sum of all elements: ",np.sum(arli))

# practice 
arr = np.array([3, 6, 9, 12, 15, 18, 21])
# 👉 Select only even number\
mask =arr%2==0
print(arr[mask])
# ================================================
arr1 = np.array([10, 22, 35, 47, 55, 70])
# 👉 Select values that are > 20 AND < 50
mask1 = (20<arr1) & (arr1<50)
print(arr1[mask1])
# ==============================================================
arr2 = np.array([-5, -2, 0, 3, -7, 8, 12])
# 👉 Change all negative numbers into 0
mask2= arr2<0
arr2[mask2]=0
print(arr2)
# ===================================================
arr = np.arange(1, 51)   # [1, 2, 3, ..., 50]
# 👉 Pick only numbers divisible by 7
mask3= arr%7==0
print(arr[mask3])
# ============================================
mat = np.array([[ 5,  2,  3],
                [ 4, 15,  6],
                [ 7,  8, 25]])
# 👉 Select only diagonal elements > 10
diagonal = np.diag(mat)
mask= diagonal>10
print(diagonal[mask])
