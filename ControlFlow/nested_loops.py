# nested_loops.py
# Example of nested loops

print("Multiplication Table (1 to 3):")

for i in range(1, 4):      # Outer loop
    for j in range(1, 4):  # Inner loop
        print(i, "*", j, "=", i * j)
    print("---")  # Separator after each row
