colors = ("red", "green", "blue", "yellow")
print("Original tuple:", colors)
# Accessing elements
print("First color:", colors[0])
print("Last color:", colors[-1])
# Tuples are immutable, so we cannot add or remove elements
# But we can concatenate tuples to create a new one
new_colors = colors + ("purple", "orange")
print("New tuple after concatenation:", new_colors)
# Slicing tuples
sliced_colors = new_colors[1:4]
print("Sliced tuple (index 1 to 3):", sliced_colors)
# Iterating through the tuple
for color in new_colors:
    print("Color:", color)

# Finding the length of the tuple
print("Length of new_colors tuple:", len(new_colors))