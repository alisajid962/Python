Dic = {"Name:": "Ali ","Age: ":"20","Education": "Se"}
# print(Dic)
# getting an element 
# print(Dic.get("Nam e:","Null"))
# print(Dic["Name:"])
#adding  
# Dic["Mind"] ="Brilliant"
# print(Dic)
# #updating
# Dic["Age: "] =25
# print(id(Dic))
# print(Dic)
#Removing Element

# Dic.pop("Mind")#Removing from where we want 
# print(Dic)
# Dic.popitem()# Remove from the last inserted key pair value
# print(Dic)

#Other useful Methods
# print(Dic.keys())
# print(Dic.values())
# print()

# print(Dic.items())

#Loop In Dictionary
# for i in Dic:
#     print(i,Dic[i])
# for i,j in Dic.items():
#     print(i,j)



# Nested Dict
# Students = {   "Student1":{"Name":"Ali Sajid","Dep":"Se"},
#                 "Student2":{"Name":"Zain Shaffique","Dep":"Optics"}          
# }
# for key in Students:
#     print(key,Students[key]["Name"])
# a = Students["Student2"]["Name"]
# print(a)

# Nested// Dictionaries with lists
my_dict = {
     "name": "Ali",
     "grades": [90, 85, 88],
     "subjects": ["Math", "Physics", "Chemistry"]

 }
print(my_dict["subjects"].append("Biology"))
print(my_dict)
# Accessing
# print(my_dict["grades"])        # [90, 85, 88]
# print(my_dict["grades"][0])     # 90

# # # Adding to list inside dictionary
# my_dict["grades"].append(95)
# print(my_dict)
