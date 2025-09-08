list = []
list.append(int(input("Enter 1 int: " )))
list.append(int(input("Enter  2nd int: " )))
list.append(int(input("Enter 3rd int: " )))
list.append(int(input("Enter 4rd int: " )))
list.append(int(input("Enter 5rd int: " )))
copy_list=list.copy()
print("copied ", copy_list)
copy_list.reverse()
print("Sorted in reverse order: ", copy_list)
if copy_list == list:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")



