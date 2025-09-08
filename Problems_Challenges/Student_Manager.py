student_data = []
name = input("Enter the student's names (Comma separated): ")
student_data.extend([n.strip().title() for n in  name.split(",")])
print("1. Search A Student")
print("2. Add A Student")
print("3. Remove A Student")
print("4. Display All Students")
choice = int(input("Enter your choice (1-5): "))
print("Your Choice: ",choice)
if choice == 1:
    name_to_search = input("Enter the name of the student to search: ").title().strip()
    if name_to_search in student_data:
        print(f"{name_to_search} is found in the student list.")
    else:
        print(f"{name_to_search} is not found in the student list.")
elif choice == 2:
      new_name =input("Enter the name you want to add:  ").title()
      student_data.append(new_name)
      print(f"{new_name} has been added to the student list.")
elif choice == 3:      
    name_to_remove = input("Enter the name of the student to remove: ").title()
    if name_to_remove in student_data:
        student_data.remove(name_to_remove)
        print(f"{name_to_remove} has been removed from the student list.")
    else:
        print(f"{name_to_remove} is not found in the student list.")
elif choice == 4:
     print("All Students: ", student_data) 

     for i, student in enumerate(student_data, start=1):
         print(f"{i}. {student}")