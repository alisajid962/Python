# single inheritance ===========================================
class animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def  speaks(self):
        print( f"{self.name} have age {self.age} speaks")
class dog(animal):
     def __init__(self, name, age):
         super().__init__(name, age)
     def speaks(self):
        print( f"{self.name} have age {self.age} speaks")    
animal1=animal("animal",34)
animal1.speaks()
bully = dog("Bulyyy",5)
bully.speaks()
print("speaks" in dog.__dict__)
# practice single inheritance================================
class vehcle:
    def __init__(self,num_wheels):
        self.num_wheels=num_wheels
    def display(self):
        print(f"the vehcle have {self.num_wheels} wheels ")
class car(vehcle):
    def __init__(self,num_wheels,brand):
        super().__init__(num_wheels)
        self.brand =brand
    def display(self):
        print(f"this {self.brand} car  has {self.num_wheels} wheels")

v = vehcle(4)
v.display()
toyota = car(6,"toyota")
toyota.display()