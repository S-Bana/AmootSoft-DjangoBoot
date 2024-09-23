"""
Calculate the sum of even and odd numbers from 0 to 100.

This script iterates through numbers from 0 to 100 (inclusive) and
calculates the sum of even and odd numbers separately.
"""

# Initialize variables to store the sum of even and odd numbers
sum_even = 0
sum_odd = 0

# Iterate through numbers from 0 to 100 (inclusive)
for number in range(101):
    if number % 2 == 0:
        # Add even numbers to sum_even
        sum_even += number
    else:
        # Add odd numbers to sum_odd
        sum_odd += number

# Print the results
print(f'Sum of odd numbers = {sum_odd} and sum of even numbers = {sum_even}')
