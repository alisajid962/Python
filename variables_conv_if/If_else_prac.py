# age = int (input("Enter Your age please: " ))
# if age >= 18 and age < 108:
#     print("You are eligible to vote.")
#     print("Your are {} years old.".format(age))
# else:
#     print("You are not eligible to vote.")



# Nested_if
# marks = int(input("Enter your marks: "))
# if marks> 50:
#      print("You have passed.")
#      if marks > 85:
#          print("You have done excellent.")
#      else:
#          print("You have done good.")
# else:
#     print("You have failed.")        



# if-else task
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: ")) 
if num1 > num2:
    print(num1)
    print("Number 1 is greater than Number 2.")
elif num2 > num1:
    print("Number 2 is greater than Number 1.")
else:
    print("Both numbers are equal.")

# even odd
# num1 = int(input("Enter a number: "))
# if num1 % 2 == 0:
#     print("Number {} is even.".format(num1) )
# else:
#     print("Number  is odd.")

# ternary if
# print("Even " if num1 % 2 == 0 else "Odd")

# task 2

num1 = int(input("Enter a number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter a third number: "))


if num1 > num2:
    if num1 > num3:
        print("Number 1 is the greatest. ")
    else:
        if num2 > num3:
            print("Number 2 is the greatest. ")
        else:
            print("Number 3 is the greatest. ")
else:
    print("the number are equal. ")
