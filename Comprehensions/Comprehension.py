# 1
pairs = [[n, n*n] for n in range(1, 11)]
print(pairs)

# 2
mat = [[1,2,3],[4,5,6],[7,8,9]]
flat = [v for nest in mat for v in nest]
print(flat)

# 3
sentence = "this is an example of list comprehensions"
words = [w for w in sentence.split() if len(w) > 3]
