# tuples.py
# Working with Tuples

coordinates = (10, 20, 30)

# Accessing elements
print("First coordinate:", coordinates[0])
print("Last coordinate:", coordinates[-1])

# Tuples are immutable
# coordinates[0] = 50  # ❌ This will give an error

# Iterating over tuple
print("Coordinates:")
for point in coordinates:
    print(point)
