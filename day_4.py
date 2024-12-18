# --- Day 4: Functions and Modules ---

# 1. Defining and Calling Functions
def greet_user(name):
    """Function to greet a user"""
    return f"Hello, {name}! Welcome to Python Programming."

def add_numbers(a, b):
    """Function to add two numbers"""
    return a + b

# Using the functions
print(greet_user("Rohan"))
result = add_numbers(10, 15)
print(f"The sum of 10 and 15 is: {result}")

# 2. Module Example: Math Module
import math

def calculate_circle_area(radius):
    """Function to calculate area of a circle using math module"""
    return math.pi * radius ** 2

radius = 5
circle_area = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} is: {circle_area:.2f}")

# 3. Using Custom Modules
# Let's simulate a custom module by defining a function in the same file
def find_factorial(num):
    """Function to find the factorial of a number"""
    return math.factorial(num)

number = 5
factorial_result = find_factorial(number)
print(f"The factorial of {number} is: {factorial_result}")

# 4. Practical Example: Checking Even or Odd Using a Function
def is_even_or_odd(number):
    """Check if a number is even or odd"""
    if number % 2 == 0:
        return "Even"
    return "Odd"

number_check = 8
print(f"{number_check} is an {is_even_or_odd(number_check)} number.")
