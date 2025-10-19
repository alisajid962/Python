from book import Book
from memeber import Member
class Library:
    def __init__(self):
        self.books=[]
        self.members=[]
    def add_book(self):
        print("--- Add New Book ---")
        book_id = input("Enter book ID: ").strip().title()
        title = input("Enter title: ").strip().title()
        author = input("Enter author: ").strip().title()
        new_Book = Book(title,author,book_id)
        self.books.append(new_Book)
        print("Book Added Successfully")
    def remove_book(self):
        print("------++-----++------")
        book_id=input("Enter the Book id : ").strip().title()
        for book in self.books:
            if book.book_id==book_id:
                self.books.remove(book)
                print("Book Removed Successfully..")
            else:
                print("Book Not Found ")
    def find_book_by_id(self):
         book_id=input("Enter the Book id : ").strip().title()
         for book in self.books:
            if book.book_id==book_id:
                return book
            else:
                print("Book Do Not Exist")
    def view_Books(self):
        if not self.books:
            print("No Books Available")
            return
        print("---Books----")
        for book in self.books:
            print(book)
# -------------------------------
# memebers
    def add_member(self):
        print()
        print("--- Register New Member ---")
        member_id = input("Enter member ID: ").strip().title()
        name = input("Enter member name: ").strip().title()
        if any(m.member_id == member_id for m in self.members):
            print("Memeber Already exist bro")
        
        new_member = Member(name, member_id)
        self.members.append(new_member)
        print("Memebr Added Succssfully...")
        return
    def find_member_by_id(self,member_id):
        for member in self.members:
            if member.member_id==member_id:
                return member
            


    # -----------------Boorrow-Return-----------
    def borrow_book(self):
        print("--- Borrow Book ---")
        member_id = input("Enter member ID: ").strip().title()
        book_id = input("Enter book ID: ").strip().title()

        member = self.find_member_by_id(member_id)
        if not member:
            print("Member not Found")
            return
        for book in self.books:
            if book.book_id==book_id:
                if book.status=="borrowed":
                    print("Book not Available")
                    return
                elif book.status=="Available":
                    book.status="borrowed"
                    member.borrowed_books.append(book)
                    print("Borrowed Succefully...")
                    return
                else:
                    print("Error Occcured")
    def return_Book(self):
        print("--- Return Book ---")
        member_id = input("Enter member ID: ").strip().title()
        book_id = input("Enter book ID: ").strip().title()
        member = self.find_member_by_id(member_id)
        if not member:
            print("Member Not Found")
            return
        for book in member.borrowed_books:
            if book.book_id == book_id:
                book.status = "available"
                member.borrowed_books.remove(book)
                print("Book returned successfully!")
                return

        print("This member didn’t borrow that book.")
        
    def save_data(self):
        try:
            with open("library_data.txt", "w") as f:
                for book in self.books:
                    f.write(f"{book.book_id},{book.title},{book.author},{book.status}\n")
            print("💾 Data saved successfully.")
        except Exception as e:
                print(f" Error saving data: {e}")

    def load_data(self):
        try:
            with open("library_data.txt", "r") as f:
                for line in f:
                    book_id, title, author, status = line.strip().split(",")
                    self.books.append(Book(book_id, title, author, status))
            print("📚 Data loaded successfully.")
        except FileNotFoundError:
            print(" No existing data found")


    def view_members(self):
        print("\n--- Library Members ---")
        if not self.members:
            print("No members registered.")
        else:
            for m in self.members:
                print(m)


                

