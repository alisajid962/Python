print("====================== List Practice ====================")
# fruits= []
# for i in range(7):
#     user_input = input(f"Enter the {i+1} Fruit: ")
#     fruits.append(user_input)
#     print(f"List after adding {i+1} element: {list}")
# print("Final List:", fruits)
print("===============================================")
marks = []
for i in range(6):
    user_input = int(input(f"Enter the marks of subject {i+1} : "))
    marks.append(user_input)
marks.sort()
print(marks.count(5))
print(marks.index(5))
print("Marks list ",marks)
print("Max marks: ",max(marks))
print("Min marks: ",min(marks))
print("Sum of marks: ",sum(marks))
print("Average of marks: ",sum(marks)/len(marks))
print("===============================================")
