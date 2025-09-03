# modules_import.py
# Example of using modules in Python

import math

# Using math module functions
print("Square root of 16:", math.sqrt(16))
print("Factorial of 5:", math.factorial(5))
print("Pi value:", math.pi)

# Importing with alias
import random as rnd
print("Random number (1-10):", rnd.randint(1, 10))

# Importing specific function
from datetime import datetime
print("Current Date & Time:", datetime.now())
