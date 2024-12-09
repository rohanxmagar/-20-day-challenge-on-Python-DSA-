print("Day 1 Challenge: Welcome to Python Basics!")

name = input("Enter your name: ")
print(f"Hello, {name}! Are you ready to start your Day 1 Python Challenge?")

length = float(input("\nChallenge 1: Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"Result: The area of the rectangle is {area}")

print("\nChallenge 2: Pattern Printing")
rows = 4
for i in range(1, rows + 1):
    print("* " * i)

radius = float(input("\nChallenge 3: Enter the radius of the circle to calculate its area: "))
circle_area = 3.14159 * radius ** 2
print(f"Result: The area of the circle is {circle_area:.2f}")

print("\nBonus Challenge: Swap two numbers!")
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
print(f"Before swapping: a = {a}, b = {b}")
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")

print("\nCongratulations on completing the Day 1 Python Challenge!")
print("Keep practicing to prepare for Day 2!")
