Name = (input("Enter Your Name: " ))
Name = Name.strip().title()
age = int(input("Enter Your Age:"))
print("Hello ",Name)
print("You are {} years old.".format(age))
if age>0:
    if age >=1 & age<=13:
        print("You get a 50% Child Discount!")
    elif age >=14 & age<=19:
        print("You get a 20% Teen Discount!")
    elif age>=20 & age <=59:
        print("You get a 10% Regular Discount.")
    else:
        print("You get a 5% Senior Citizen Discount!")
else:
    print("Invalid age entered. Please enter a positive number.")
    SystemExit            
    