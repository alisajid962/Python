 implicit type conversion
 x= 5
 y= 10.6
 z= x + y    
 print(z ,type(z))
#  explicit type conversion
 z= x + int(y)
 print(z ,type(z))
#  ask users for input two numbers as strings and convert into integers
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
 print(num1+num2)  # This will concatenate the strings
 num1= int(num1)
 num2= int(num2)
 print(num1+num2) # This will print the sum of the two integers
print("Product: ", num1*num2)
#CONSTANTS
 import constant as const
 print("Name: ",const.NAME)
 print("City: ",const.CITY)
#Arithematic operations
 print("Sum: ", num1 + num2)
 print("Difference: ", num1 - num2)
 print("Multiplication: ", num1 * num2)
 print("Division: ", num1 / num2)

 #Comparison Operators
 print("Equal: ", num1 == num2)
 print("Not Equal: ", num1 != num2)
 print("Greater: ", num1 > num2)
 print("Less: ", num1 < num2)
 print("Greater than equal to: ",num1>=num2)
 print("Less than equal to: ",num1<=num2)



#  logical operators (AND OR NOT )
 a=4
 b=7
 print(a>b and a<b)
 print(a>b or a<b)
 print(not(a>b))

#  aSSIGNMET OPERATOR
int a = 10
 a+=a#addition assignment opr
 print(a)
 a-=a#subtraction assignment opr
print(a)