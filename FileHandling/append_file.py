# append_file.py
# Appending data to an existing file

with open("output.txt", "a") as file:
    file.write("This line is appended to the file.\n")

print("New line appended to output.txt")
