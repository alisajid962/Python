class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print(f"Tile is : {self.title} and Author({self.author})")
    @classmethod
    def copy(cls,other_obj):
        return cls(other_obj.title,other_obj.author)
    
book1=book("jarvis","Ali SAjid")
book2=book.copy(book1)
book1.display()
book2.display()
book2.display()
book2.display()
book2.display()