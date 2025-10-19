class Book:
    def __init__(self,title,author,book_id,status="Available"):
        if not isinstance(title,str):
            print("Title Must Be String")
        if not isinstance(author,str):
            print("Author Must Be String")
        if not isinstance(author,str):
            print("Status Must Be Boolean")

        self.title=title
        self.author=author
        self.book_id=book_id
        self.status=status
    def __str__(self):
        return f"Book id: {self.title} by {self.author}-Status: {self.status}"
    

        
       