# dictionaries.py
# Working with Dictionaries

person = {
    "name": "Alice",
    "age": 21,
    "city": "New York"
}

# Accessing values
print("Name:", person["name"])
print("Age:", person.get("age"))

# Adding a new key-value pair
person["email"] = "alice@example.com"
print("After adding email:", person)

# Updating value
person["age"] = 22
print("After updating age:", person)

# Removing a key
person.pop("city")
print("After removing city:", person)

# Iterating through dictionary
print("Dictionary contents:")
for key, value in person.items():
    print(key, ":", value)
