"""
Reverse a list of fruits.

This script demonstrates how to reverse a list manually using a for loop
and list indexing, without using built-in reverse functions or slicing.
"""

# Original list of fruits
original_list_fruits = ['apple', 'banana', 'orange', 'cucumber', 'pineapple']

# Initialize an empty list to store the reversed fruits
reversed_list_fruits = []

# Iterate through the original list in reverse order
for index in range(len(original_list_fruits) - 1, -1, -1):
    # Append each fruit to the reversed list
    reversed_list_fruits.append(original_list_fruits[index])

# The second way ==================================================

# Iterate through the original list in reverse order
# for index in reversed(original_list_fruits):
    # reversed_list_fruits.append(index)

# Print the original and reversed lists
print("Original list of fruits:")
print(original_list_fruits)
print("\nReversed list of fruits:")
print(reversed_list_fruits)
