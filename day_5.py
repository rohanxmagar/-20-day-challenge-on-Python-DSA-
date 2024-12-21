# --- Day 5: Lists and List Operations ---

# 1. Creating and Accessing Lists
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("Original List of Fruits:", fruits)

# Accessing elements by index
print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

# Slicing the list
print("First Three Fruits:", fruits[:3])
print("Fruits from Index 2 Onwards:", fruits[2:])

# 2. Modifying Lists
fruits.append("fig")  # Adding an element
print("\nList After Adding 'fig':", fruits)

fruits.remove("banana")  # Removing an element
print("List After Removing 'banana':", fruits)

fruits[1] = "blueberry"  # Modifying an element
print("List After Replacing 'cherry' with 'blueberry':", fruits)

# 3. List Operations
numbers = [1, 2, 3, 4, 5]

# Sum of all elements
print("\nSum of Numbers:", sum(numbers))

# Checking membership
print("Is 3 in the list?", 3 in numbers)

# Sorting the list
numbers.sort(reverse=True)
print("List in Descending Order:", numbers)

# 4. Practical Example: Finding the Largest Element
largest_number = max(numbers)
print("\nLargest Number in the List:", largest_number)

# 5. Nested Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\nNested List (Matrix):", matrix)
print("Element at Row 1, Column 2:", matrix[0][1])  # Accessing nested list elements

# 6. Using a Loop to Process Lists
squared_numbers = [num ** 2 for num in numbers]
print("\nSquared Numbers:", squared_numbers)
