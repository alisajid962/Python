students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add a student")
    print("2. Remove a student")
    print("3. Search for a student")
    print("4. Display all students")
    print("5. Exit")
    print("=====================================")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
         name = input("Enter your Name: ").strip().title()
         if name:  # checks name is not empty
            students.append(name)
            print("✅ Student Added Successfully!")
         else:
            print("❌ Please enter a valid name.")


    elif choice == '2':
        # TODO: Remove a student
        name_remove = input("Enter ther name of the student to remove: ").strip().title()
        removed=False
        if name_remove in [name.strip().title() for name in students]:
            students.remove(name_remove)
        if not removed:
            print("Student Does Not exist")

            


    elif choice == '3':
        # TODO: Search for a student
        found = False
        search_name=input("Enter the name you want to search: ").strip().title()
        if search_name in [name.strip().title() for name in students]:
            print("Studnet Found in the List at index",students.index(search_name))
            found=True
            break
        if not found:
            print("Studnet Not Found")
    elif choice == '4':
        # TODO: Display all students
         print(students)
        

    elif choice == '5':
        print("👋 Exiting program...")
        break

    else:
        print("❌ Invalid choice! Please try again.")
