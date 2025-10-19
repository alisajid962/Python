def decorator(func):
    print("Decorator runs once during setup.")
    def wrapper():
        print("Wrapper runs every time you call the function.")
        func()
    return wrapper

@decorator
def greet():
    print("Hello!")


greet()
greet()
greet()
greet()
greet()
def square(x):
    return x * x

numbers = (1, 2, 3, 4, 5)

result = map(square, numbers)
print(result)           # <map object at 0x...>
print(list(result))     # [1, 4, 9, 16, 25]

