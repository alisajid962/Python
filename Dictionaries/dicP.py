dic ={}
# Example structure
dic = {
    "S1": {"name": "Ali", "marks": {"Math": 85, "Physics": 90}, "age": 20},
    "S2": {"name": "Sana", "marks": {"Math": 95, "Physics": 92}, "age": 19},
    "S3": {"name": "Ahmed", "marks": {"Math": 70, "Physics": 75}, "age": 21}
}

for key,info in dic.items():
    print(f"Student Id {key}")
    print(f"Name: {info["name"]}")
    print(f"Age:  {info["age"]}")
    print("Marks: ")
    for sub,marks in info["marks"].items():
        print(f"{sub} :  {marks}")
    print("-------------")
