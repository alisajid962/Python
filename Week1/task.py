students = [("Ali", 85), ("Sara", 90), ("Hassan", 85), ("Fatima", 92)]
names=[name for name,marks in students]
print("Students: ",names)
# for name,marks in students:
#    names.append(name)

marks={mark for name,mark in students}
print("Uniques Marks:",marks)
# for tup in students:
#    name,grades =tup
#    marks.add(grades)

max=0
for name,marks in students:
    if max<marks:
        max=marks
print("Max Marks: ",max)

min=students[0][1]
for name,marks in students:
    if min>marks:
        min=marks
    
print("Min Marks: ",min)

def  add_student():
    name=input(("Enter the Name oF the Student: ")).strip().title()
    marks=int(input("Enter The Marks Of the Students: "))
    temp = (name,marks)
    students.append(temp)
    print(students)
    print("Student Addded ")
       
add_student()


