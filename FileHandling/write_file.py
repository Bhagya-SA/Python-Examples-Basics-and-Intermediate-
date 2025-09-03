# write_file.py
# Writing to a file (this will overwrite existing content)

with open("output.txt", "w") as file:
    file.write("Hello, this is a new file.\n")
    file.write("This file was created using Python.\n")

print("Data written to output.txt")
