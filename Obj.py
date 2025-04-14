# Define a list (mutable object)
a = [1, 2, 3]

# b references the same object as a
b = a

# Modify the object using b
b[0] = 100

# Both a and b see the change
print("a:", a)  # Output: a: [100, 2, 3]
print("b:", b)  # Output: b: [100, 2, 3]
