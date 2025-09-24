students={}
print(type(students))
n=int(input("How many studnets you want to enter: "))
for i in range(n):
    name=input(f"Enter the Name of {i+1} Studnet: ")
    marks =int(input("Enter the marks of {name} student: "))
    students[name]=marks
def display(student):
    for key,values in  student.items():
        print(f"The {key} ontained {marks}")

def findmax(student):
    max=0
    topper_name=None
    for key,value in  student.items():
        if value >max:
            max = value
            topper_name=key
        
    print(f"the max marks student is {key } with marks {value}")

display(students)
findmax(students)

