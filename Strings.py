#Strings are sequence of char
# text = 'University is starting from september'
# name= 'Dahranwala'

# indexing
# print(text[0])
# print(text[1])
# #negative indexing
# print("Negative index") 
# print(text[-1])

#slicing
# print(text[0:5])
# new_city = name[1:4] # end is not included
# print("assigning slicing")
# print(new_city)
# print(text[7:]) # go to last
# print(text[:5]) # start from 0




# #copying string
# copied_text = name[:]
# print("copying string")
# print(copied_text)




name = input("Enter your name: ")
print(name[::-1]) # start from end to start
print(name[0:4])#first three chracter 
print(name[:]) # copy the whole string
print(name[-3:]) # last three character
print(name[::2])
print(id(name)) # memory address


# # String formatting 
# name = input("Enter your name: ")
# city = input("Enter your city: ")
# print(f"Hello, {name}")
# # format method
# print("Hello, {} from {}".format(name,city))
