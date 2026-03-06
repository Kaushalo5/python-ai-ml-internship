# list comprehension
numbers = [1,2,3,4,5]
squares = [n*n for n in numbers]
print("Squares:", squares)

# lambda function
add = lambda a,b: a+b
print("Lambda sum:", add(5,7))

# decorator
def logger(func):
    def wrapper(*args, **kwargs):
        print("Running function:", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name):
    print("Hello", name)

greet("Kaushal")

# generator
def countdown(n):
    while n>0:
        yield n
        n-=1

print("Generator output:")
for i in countdown(5):
    print(i)