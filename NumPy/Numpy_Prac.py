import numpy as np
list1 = [[1,2,3,7],[4,5,6,7]]
arr1 =np.array(list1)
print(arr1)
print()
# =============================
arr2= np.arange(5)
print(arr2)
print()

arr3=np.zeros(9)
arr33=np.zeros((3,2))
arr4=np.ones(5)
arr44=np.ones((4,1))
print(arr3)
print(arr33)
print(arr4)
print(arr44)
# =========================
# linsp=np.linspace(0,1,1000)
# print(linsp)
# =========================================
asym=np.eye(7)
print(asym)   #return symettric idenity matrix
# ========================================
# randoms
ran =np.random.rand(5,5)
ran1=np.random.random(5)
print(ran)
print(ran1)
ran2 =np.random.randn(4,4)
print(ran2)
ran3 =np.random.randint(1,100)
print(ran3)
ran4=np.random.randint(1,100,10)
print(ran4)
rarr=np.array(ran4)
print(rarr[0:5],rarr[3])
print(ran4.argmax())
