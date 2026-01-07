a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
c= int(input("Enter third number: "))

if a>b and a>c:
    print(f"{a} is the greatest number")
elif b>a and b>c:
    print(f"{b} is the greatest number")
else:
    print(f"{c} is the greatest number")    


from random import randint
num1 = randint(1, 100)
num2 = randint(1, 100) 
print(f"Random numbers generated are {num1} and {num2}")