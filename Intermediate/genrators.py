# generators.py
# Example of Generators in Python

def countdown(n):
    while n > 0:
        yield n   # yield returns one value at a time
        n -= 1

# Using the generator
for number in countdown(5):
    print(number)

# Generator expression (like list comprehension but with ())
squares_gen = (x * x for x in range(1, 6))
print("Squares using generator expression:")
for sq in squares_gen:
    print(sq)
