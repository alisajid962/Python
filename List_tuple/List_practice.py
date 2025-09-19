print("====================== List Practice ====================")
# fruits= []
# for i in range(7):
#     user_input = input(f"Enter the {i+1} Fruit: ")
#     fruits.append(user_input)
#     print(f"List after adding {i+1} element: {list}")
# print("Final List:", fruits)
# print("===============================================")
# marks = []
# for i in range(6):
#     user_input = int(input(f"Enter the marks of subject {i+1} : "))
#     marks.append(user_input)
# marks.sort()
# print(marks.count(5))
# print(marks.index(5))
# print("Marks list ",marks)
# print("Max marks: ",max(marks))
# print("Min marks: ",min(marks))
# print("Sum of marks: ",sum(marks))
# print("Average of marks: ",sum(marks)/len(marks))
print("===============================================")
a = [1, 2, 3, 4, 5]
print(len(a))
a.append([11,12])
a.extend([10,19,1])
print(a.pop())
print(a.pop(1))
# print(a.index(2)) # List of integers
b = ['apple', 'banana', 'cherry'] # List of strings
c = [1, 'hello', 3.14, True] # Mixed data types
print(a[4][1])
print(a)
print()
print(b)
print(c)
