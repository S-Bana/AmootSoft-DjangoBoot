"""
This Python script demonstrates the creation and manipulation of tuples.
It defines three separate tuples: fruit, food, and drink.
Then, it merges these tuples into a single tuple called merged_tuple.
Next, it creates a new tuple called tuple_ by concatenating merged_tuple with two additional elements: 'chery' and 'ice_coffee'.
Finally, it extracts a slice of tuple_ containing the first 9 elements and assigns it to my_favorite, which is then printed.
"""

# Define the fruit tuple
fruits = ('apple', 'banana', 'orange')

# Define the food tuple
foods = ('pizza', 'aush', 'pasta')

# Define the drink tuple
drinks = ('water', 'coffee', 'tea')

# Merge the fruit, food, and drink tuples into a single tuple
merged_tuple = fruits + foods + drinks

# Create a new tuple by concatenating merged_tuple with two additional elements
tuple_with_additions = merged_tuple + ('cherry', 'ice_coffee')

# Extract a slice of tuple_with_additions containing the first 9 elements
my_favorite = list(tuple_with_additions[5:8])

# Print the my_favorite tuple
print(f"list :{my_favorite} type:{type(my_favorite)}")
