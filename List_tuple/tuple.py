# tuple1 = ("ALi Sajid",1,2,3,4,5,6)
# tuple12=("Ali Sajid",)
# print(tuple12[1:5])
# print("Tuple",id(tuple1))
# tuple1[0] = 10 # tuples are immutable
# print("Tuple",id(tuple1))
# print(type(tuple1))
# print(tuple1[0])
# print(tuple1[1:])
# # tuple1[0] = 10 # tuples are immutable
# print("count")
# print(tuple1.count(2))
# print(tuple1.index(4))
# print(len(tuple1))
# # tuple unpacking
# a,b,c,d,e,f = tuple1
# print(a)
# print(b)
# print(c)
# print(d)
# print(tuple1[0])

Books = (("Rich Dad Poor Dad", "Robert Kiyosaki", 1997),
         ("The Intelligent Investor", "Benjamin Graham", 1949),
         ("To Kill a Mockingbird", "Harper Lee", 1960),
         ("Hush  Little Baby", "George Orwell", 1949),
         ("The Great Gatsby", "F. Scott Fitzgerald", 1925)
)
for title,author,year in Books:
        print(f"Title: {title} , Author: {author}, Year: {year}")
title1,author1,year1 = Books[0]
print(f"Title: {title1}, Author: {author1}, Year: {year1}")
t = 1, "apple", 3.14
print(t)
print(type(t))