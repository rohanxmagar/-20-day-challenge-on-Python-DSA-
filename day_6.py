# --- Day 6: Tuples and Tuple Operations ---

# 1. Creating and Accessing Tuples
fruits = ("apple", "banana", "cherry", "date", "elderberry")
print("Original Tuple of Fruits:", fruits)

# Accessing elements by index
print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

# Slicing the tuple
print("First Three Fruits:", fruits[:3])
print("Fruits from Index 2 Onwards:", fruits[2:])

# 2. Tuple Operations
numbers = (1, 2, 3, 4, 5)

# Finding the length of the tuple
print("\nLength of Numbers Tuple:", len(numbers))

# Checking membership
print("Is 3 in the tuple?", 3 in numbers)

# Finding the maximum and minimum values
print("Maximum Number:", max(numbers))
print("Minimum Number:", min(numbers))

# Concatenating tuples
extra_numbers = (6, 7, 8)
concatenated_tuple = numbers + extra_numbers
print("\nConcatenated Tuple:", concatenated_tuple)

# 3. Tuple Unpacking
person = ("Rohan", 20, "BCA")
name, age, course = person
print("\nTuple Unpacking Example:")
print(f"Name: {name}, Age: {age}, Course: {course}")

# 4. Practical Example: Counting and Indexing
repeated_numbers = (1, 2, 3, 1, 4, 1, 5)

# Counting occurrences of an element
count_of_ones = repeated_numbers.count(1)
print("\nNumber of occurrences of 1:", count_of_ones)

# Finding the index of an element
index_of_three = repeated_numbers.index(3)
print("Index of the number 3:", index_of_three)

# 5. Using a Loop with Tuples
print("\nIterating through the tuple:")
for fruit in fruits:
    print(f"- {fruit}")
