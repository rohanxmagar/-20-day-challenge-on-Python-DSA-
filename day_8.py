# --- Day 8: Sets and Set Operations ---

# 1. Creating and Displaying Sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Set A:", set_a)
print("Set B:", set_b)

# 2. Basic Set Operations
# Union
union_set = set_a | set_b
print("\nUnion of A and B:", union_set)

# Intersection
intersection_set = set_a & set_b
print("Intersection of A and B:", intersection_set)

# Difference
difference_set = set_a - set_b
print("Difference (A - B):", difference_set)

# Symmetric Difference
symmetric_difference_set = set_a ^ set_b
print("Symmetric Difference of A and B:", symmetric_difference_set)

# 3. Adding and Removing Elements
set_a.add(6)  # Adding an element
print("\nSet A After Adding 6:", set_a)

set_a.discard(1)  # Removing an element
print("Set A After Discarding 1:", set_a)

# 4. Practical Example: Removing Duplicates from a List
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("\nRemoving Duplicates from List:", unique_numbers)

# 5. Checking Membership
print("\nIs 4 in Set A?", 4 in set_a)
print("Is 10 in Set B?", 10 in set_b)

# 6. Iterating Over a Set
print("\nIterating Through Set A:")
for element in set_a:
    print(f"- {element}")
