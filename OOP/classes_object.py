# classes_objects.py
# Example of Class and Object

class Student:
    # Constructor (__init__) to initialize object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects
s1 = Student("Alice", 21)
s2 = Student("Bob", 22)

# Calling methods
s1.display()
s2.display()
