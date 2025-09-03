# lists.py
# Working with Lists

fruits = ["apple", "banana", "cherry"]

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding elements
fruits.append("orange")
print("After append:", fruits)

# Removing elements
fruits.remove("banana")
print("After removing banana:", fruits)

# Iterating over list
print("Fruits list:")
for fruit in fruits:
    print(fruit)
