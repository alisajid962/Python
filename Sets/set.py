set1= set()
print(type(set1))


# s = {1,2,3}
# print(s)
# s.add(4)
# print(s)
# s.update([5,6])
# print(s)
# s.remove(2)
# s.discard(3)
# print(s)




# s.add(4)        # Add one element
# print(s)        # {1, 2, 3, 4}

# s.update([5, 6]) # Add multiple elements
# print(s)        # {1, 2, 3, 4, 5, 6}

# s.remove(3)     # Removes 3 (error if not found)
# print(s)

# s.discard(10)   # Removes safely (no error if missing)
# print(s)

# s.pop()         # Removes a random element
# print(s)

# s.clear()       # Removes all elements
# print(s)
s1  = {1,2,3,4,5}
s2 = {4,5,6,7,8,9}
print(s1 | s2)           #union
print(s1 & s2)    #interseciton
print(s1 - s2) # diffrence 
print(s1.issubset(s2)) 