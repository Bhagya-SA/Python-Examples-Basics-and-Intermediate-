# read_file.py
# Reading a file

# Make sure a file named "sample.txt" exists in the same folder
# with some text inside it before running this program.

with open("sample.txt", "r") as file:
    content = file.read()       # Reads the whole file
    print("File Content:\n", content)

# Reading line by line
with open("sample.txt", "r") as file:
    print("\nReading line by line:")
    for line in file:
        print(line.strip())
