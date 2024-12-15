# Day 2: Basic Data Types and Operators - "Data Delve"

#1. Strings
name = "Rohan"
greeting = "Welcome to Python!"
full_message = greeting + " " + name
print("String Example:")
print(full_message)

#2. Lists
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print("\nList Example:")
print("Numbers List:", numbers)
print("First number in the list:", numbers[0])

#3. Tuples
coordinates = (10, 20) 
print("\nTuple Example:")
print("Coordinates Tuple:", coordinates)
print("X Coordinate:", coordinates[0]) 

#4. Dictionary
student = {"name": "Rohan", "age": 20, "course": "BCA"}
print("\nDictionary Example:")
print("Student Dictionary:", student)
print("Student's Name:", student["name"]) 

#5. Arithmetic Operators
a = 10
b = 5
print("\nArithmetic Operators Example:")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

#6. Comparison Operators 
print("\nComparison Operators Example:")
print(f"Is {a} greater than {b}? {a > b}")
print(f"Is {a} equal to {b}? {a == b}")
print(f"Is {a} less than or equal to {b}? {a <= b}")

#7. Logical Operators
x = True
y = False
print("\nLogical Operators Example:")
print(f"Is x AND y True? {x and y}")
print(f"Is x OR y True? {x or y}")
print(f"Is NOT x True? {not x}")

#8. Type Casting
print("\nType Casting Example:")
str_value = str(a)  
int_value = int("100")  
print(f"Integer to String: {str_value}")
print(f"String to Integer: {int_value}")

print("\nDay 2 Challenge completed! You've learned about data types and operators in Python.")
