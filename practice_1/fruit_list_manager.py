"""
This Python script prompts the user to enter their favorite fruit and checks if it is in a predefined list of fruits.
If the entered fruit is already in the list, it informs the user that the fruit is included. 
If the fruit is not in the list, it adds the fruit to the list. 
Finally, it prints the updated list of fruits.
"""

# Prompt the user to enter their favorite fruit
favorite_fruit = input('Enter your favorite fruit: ')

# Predefined list of fruits
fruit_list = ['apple', 'banana', 'orange']

# Check if the user's favorite fruit is in the predefined list
if favorite_fruit in fruit_list:
    print(f'This fruit is in the list: {fruit_list}')
else:
    fruit_list.append(favorite_fruit)  # Add the fruit to the list if it's not already present

# Print the updated list of fruits
print(f"This fruit is not in the list, it was added to the list:{fruit_list}")
