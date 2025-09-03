# sets.py
# Working with Sets

numbers = {1, 2, 3, 4, 2, 3}  # Duplicates are automatically removed
print("Set:", numbers)

# Adding elements
numbers.add(5)
print("After adding 5:", numbers)

# Removing elements
numbers.discard(2)
print("After discarding 2:", numbers)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
