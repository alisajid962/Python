class Member:
    def __init__(self,name,member_id):
        if not isinstance(name,str) or not isinstance(member_id,str):
            print(f"Name and Id must be String {member_id}")
        self.name=name 
        self.member_id=member_id
        self.borrowed_books=[]
    def __str__(self):
        return f"{self.name} : ({self.member_id})"
    
    
        