# --- Day 3: Control Structures (If-Else, For Loops) ---

number = int(input("Enter a number: "))

if number > 0:
    print(f"{number} is a Positive number.")
elif number < 0:
    print(f"{number} is a Negative number.")
else:
    print(f"{number} is Zero.")

# 2. FOR LOOP Example: Print numbers in a range
print("\nNumbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")

# 3. IF-ELSE + FOR LOOP: Find even and odd numbers in a list
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\n\nEven and Odd Numbers:")

for num in numbers_list:
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# 4. Practical Example: Calculate the sum of numbers from 1 to N
n = int(input("\nEnter a number N to calculate the sum from 1 to N: "))
total_sum = 0

for i in range(1, n + 1):
    total_sum += i

print(f"The sum of numbers from 1 to {n} is: {total_sum}")

# 5. BONUS: Nested IF-ELSE and FOR LOOP
print("\nNested IF-ELSE Example: Multiples of 3 and 5")
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}: Divisible by both 3 and 5")
    elif i % 3 == 0:
        print(f"{i}: Divisible by 3")
    elif i % 5 == 0:
        print(f"{i}: Divisible by 5")
    else:
        print(f"{i}: Not divisible by 3 or 5")
