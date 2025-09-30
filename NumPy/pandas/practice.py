import pandas as pd
index1=["a","b","c","d","e","f","g","h","i"]
list =[1,2,3,4,5,6,7,8,9]
# ds=pd.Series(list,index=index1)
# # ds["b"]=88
# # print(ds["a"])
# print(ds[0])
# print(ds)
dic ={
    "names":["Ali","Qazi","Adnan","Zain","Hassan"],
    "age":[19,20,22,33,36],
    "city":["sahiwal","harrapa","kabirwala","dahranwala","null"]
}

df = pd.DataFrame(dic)
print(df)
# s1 = pd.Series(["Ali", "Sara", "John"], name="Name")
# print("s1",s1)
# s2 = pd.Series([22, 25, 24], name="Age")
# s3 = pd.Series([85, 90, 95], name="Marks")

# df = pd.concat([s1, s2, s3], axis=1)
# print(df)
