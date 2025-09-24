class student:
    total__students=0
    def __init__(self,name="Unknown",age="Not provided"):
        self.name=name
        self.age=age
        student.total__students=student.total__students+1
    
    def display(self):
        print(f"{self.name} is {self.age} years old. ")
    @classmethod
    def total_studemts(cls):
        print(f"Total students are:  {cls.total__students}")
s1=student("Ali  Sajid",50)
s2=student("Qazi",30)
s1.display()
s2.display()
student.total_studemts()

        