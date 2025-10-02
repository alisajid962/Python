import numpy as np
import pandas as pd

index1=["a","b","c","d","e","f","g","h","i"]
list =[1,2,3,4,5,6,7,8,9]

# ds=pd.Series(list,index=index1)
# # ds["b"]=88
# # print(ds["a"])
# print(ds[0])
# print(ds)


# dic ={
#     "names":["Ali","Qazi","Adnan","Zain","Hassan"],
#     "age":[19,20,22,33,36],
#     "city":["sahiwal","harrapa","kabirwala","dahranwala","null"]
# }
# df = pd.DataFrame(dic)
# print(df.loc[0]["age"])
# print(df)
# df.to_csv("panda.csv")



# data = [ ["Ali", 22, 85], ["Sara", 25, 90],   ["John", 24, 95]]
# df = pd.DataFrame(data, columns=["Name", "Age", "Marks"])
# print(df)



# s1 = pd.Series(["Ali", "Sara", "John"], name="Name")
# print("s1",s1)
# s2 = pd.Series([22, 25, 24], name="Age")
# s3 = pd.Series([85, 90, 95], name="Marks")
# df = pd.concat([s1, s2, s3], axis=1)
# print(df)
index =["a","b","c","d","e","f","g","h","i","j"]
df = pd.DataFrame(np.arange(100).reshape(10,10),columns=index)
print(df)
print(df.head())
print(df.tail(3))
print(df.describe())
print(df.info())
