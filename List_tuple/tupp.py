students=[]
no_of_stud=int(input("Enter How Many Students you want to enter: "))
for i in range(no_of_stud):
    name=input("Enter The Name of the stud: ").strip().title()
    marks=int(input("Enter the Marks Of the Students: "))
    stu_tup=(name,marks)
    students.append(stu_tup)

for tup in students:
    print(f"Name: {tup[0]}  marks: {tup[1]}")

print(f"Total Number Of Students is : {len(students)}")

for tup in students:
    max=tup[1]
    if max>tup[1]:
        max=tup[1]
print("The max marks is : ",max)


