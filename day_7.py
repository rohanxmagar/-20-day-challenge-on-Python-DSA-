# --- Day 7: Dictionaries and Dictionary Operations ---

# 1. Creating and Accessing Dictionaries
student = {"name": "Rohan", "age": 20, "course": "BCA"}
print("Original Dictionary:", student)

# Accessing values using keys
print("Student's Name:", student["name"])
print("Student's Age:", student["age"])

# Using the get() method
print("Student's Course (using get):", student.get("course"))

# 2. Adding and Updating Entries
student["grade"] = "A"  # Adding a new key-value pair
print("\nDictionary After Adding Grade:", student)

student["age"] = 21  # Updating an existing value
print("Dictionary After Updating Age:", student)

# 3. Removing Entries
student.pop("grade")  # Removing a key-value pair
print("\nDictionary After Removing Grade:", student)

del student["course"]  # Deleting a key-value pair
print("Dictionary After Deleting Course:", student)

# 4. Iterating Through Dictionaries
print("\nIterating Through Dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")

# 5. Practical Example: Word Frequency Counter
sentence = "python is amazing and python is fun"
word_counts = {}

for word in sentence.split():
    word_counts[word] = word_counts.get(word, 0) + 1

print("\nWord Frequency Counter Example:")
print(word_counts)

# 6. Using a Dictionary for Mapping
phonebook = {
    "Rohan": "123-456-7890",
    "Aditi": "987-654-3210",
    "Kabir": "555-555-5555"
}

print("\nPhonebook Example:")
print("Rohan's Phone Number:", phonebook["Rohan"])
