# Creating a dictionary
student = {
    "name": "John",
    "age": 21,
    "grades": [85, 90, 78]
}

# Accessing values
print(student["name"])     # John
print(student["age"])      # 21

# Adding a new key-value pair
student["school"] = "MIT"

# Updating an existing value
student["age"] = 22

# Looping through keys
for key in student:
    print(key, ":", student[key])

# Getting only keys
print(student.keys())

# Getting only values
print(student.values())

# Getting key-value pairs
print(student.items())
