class student:
    list=[]
    count=0
    def __init__(self,name,age,marks):
        self.name=name
        if age >0:
            self.age=age
        self.marks=marks
        student.count +=1
    def addStudent():
        name =input("Enter Name: ")
        age =int(input("Enter Age: "))
        marks =int(input("Enter the marks: "))
        new_Student=student(name,age,marks)
        student.list.append(new_Student)
    def viewstudent():
        for stud in student.list:
            print(f"\nName: {stud.name}  \nAge: {stud.age}  \nmarks: {stud.marks}")
    def searchStudent():
        name_to_search = input("Enter Name to Search: ")
        name_to_search=name_to_search.lower()
        for stu in student.list:
         
            if(name_to_search==stu.name.lower()):
                print(f"\nName: {stu.name}  \nAge: {stu.age}  \nmarks: {stu.marks}")
            else:
                print("Student Not Found.")
    def highestMarksStudent():
       print( topper=max(student.list,key=lambda s:s.marks))

class management(student):
    print("\n===== Student Management Menu =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Show Highest Marks Student")
    print("4.Search Student")
    print("4. Exit")
while True:

    choice = input("Enter your choice: ")
    if choice == "1":
        student.addStudent()
    elif choice == "2":
        student.viewstudent()
    elif choice == "3":
        student.highestMarksStudent()
    elif choice == "4":
        student.searchStudent()
        break
    elif choice == "5":
        print("Exit....  GoodBye")
    else:
        print("⚠ Invalid choice. Please try again.")



