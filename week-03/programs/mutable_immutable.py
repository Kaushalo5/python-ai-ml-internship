# Mutable example
list_a = [1, 2, 3]
list_b = list_a
list_b.append(4)


# Immutable example
x = 10
y = x
y = 20

print("x:", x)
print("y:", y)
print("List B:", list_b)
print("List A after modifying List B:", list_a)

