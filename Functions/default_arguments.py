# default_arguments.py
# Function with default argument

def greet(name="Guest"):
    """This function greets a person, default is 'Guest'."""
    print("Hello,", name)

# Calling with argument
greet("Alice")

# Calling without argument
greet()
