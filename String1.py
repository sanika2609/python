# Take input from the user
user_input = input("Enter a sentence: ")

# Replace a word in the string
replaced = user_input.replace("Python", "Java")
print("After replacement:", replaced)

# Split the sentence into words
words = user_input.split()
print("Words list:", words)

# Count how many words
print("Number of words:", len(words))

# Join the words back with hyphens
joined = "-".join(words)
print("Hyphen-joined string:", joined)

# Check if string starts or ends with certain words
print("Starts with 'Hello'? ", user_input.startswith("Hello"))
print("Ends with 'world'? ", user_input.endswith("world"))
