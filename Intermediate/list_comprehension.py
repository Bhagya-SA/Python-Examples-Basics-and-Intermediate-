# list_comprehension.py
# Example of List Comprehension

# Normal way
squares = []
for i in range(1, 6):
    squares.append(i * i)
print("Squares using loop:", squares)

# Using list comprehension
squares_comp = [i * i for i in range(1, 6)]
print("Squares using comprehension:", squares_comp)

# Filtering with comprehension
even_numbers = [i for i in range(10) if i % 2 == 0]
print("Even numbers:", even_numbers)
