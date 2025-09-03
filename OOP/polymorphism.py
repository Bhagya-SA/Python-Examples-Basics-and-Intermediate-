# polymorphism.py
# Example of Polymorphism in Python

class Bird:
    def fly(self):
        print("Birds can fly.")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies fast.")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly.")

# Polymorphism in action
birds = [Bird(), Sparrow(), Penguin()]

for bird in birds:
    bird.fly()
