# main.py
from library import Library

def main():
    lib = Library()
    lib.load_data()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. View All Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Add Member")
        print("5. View Members")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Save and Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                lib.view_Books()
            elif choice == 2:
                lib.add_book()
            elif choice == 3:
                lib.remove_book()
            elif choice == 4:
                lib.add_member()
            elif choice == 5:
                lib.view_members()
            elif choice == 6:
                lib.borrow_book()
            elif choice == 7:
                lib.return_Book()
            elif choice == 8:
                lib.save_data()
                print("👋 Exiting system. Goodbye!")
                break
            else:
                print("❌ Invalid choice. Try again.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    main()
