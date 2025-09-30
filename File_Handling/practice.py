import csv
with open("info.csv", "r") as file:
    reader = csv.reader(file)
    print(reader)
    for col in reader:
        print(col)

# with open("info.csv",("r")) as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
#         print(row)
 
data = [
    ["id", "name", "age", "grade"],
    [1, "Ali", 20, "A"],
    [2, "Sara", 21, "B"],
    [3, "Hamza", 19, "A"]
]
with open("new_students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerows(data)



with open("students_dict.csv", "w", newline="") as file:
    fieldnames = ["id", "name", "age", "grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"id": 1, "name": "Ali", "age": 20, "grade": "A"})
    writer.writerow({"id": 2, "name": "Sara", "age": 21, "grade": "B"})
