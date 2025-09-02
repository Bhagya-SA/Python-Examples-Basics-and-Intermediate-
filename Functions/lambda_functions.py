# lambda_functions.py
# Using lambda (anonymous) functions

# Normal function
def square(n):
    return n * n

# Lambda function for square
square_lambda = lambda n: n * n

# Lambda function for addition
add = lambda a, b: a + b

print("Square using normal function:", square(5))
print("Square using lambda:", square_lambda(5))
print("Addition using lambda:", add(3, 7))
