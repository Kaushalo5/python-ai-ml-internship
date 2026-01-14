n = int(input("Enter a number: "))

if n % 2 == 0:
    print(n, "is Even")
else:
    print(n, "is Odd")

print(f"{n} is even" if n % 2 == 0 else f"{n} is odd")