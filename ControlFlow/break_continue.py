# break_continue.py
# Demonstrating break and continue in loops

print("Using break:")
for i in range(1, 10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    print("i =", i)

print("\nUsing continue:")
for i in range(1, 6):
    if i == 3:
        print("Skipping i =", i)
        continue
    print("i =", i)
