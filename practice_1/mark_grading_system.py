"""
This Python script prompts the user to enter a numerical mark and then categorizes the mark into one of the following groups:
- Group A: 80 to 100
- Group B: 70 to 89
- Group C: 60 to 69
- Group D: 50 to 59
- Group F: 0 to 49
If the entered mark is not within the valid range, an error message is displayed.
"""

# Prompt the user to enter a numerical mark
user_mark = int(input('Enter your mark: '))

# Check the user's mark and print the corresponding grade group
if 80 <= user_mark <= 100:
    print('Your mark is in Group A.')
elif 70 <= user_mark <= 89:
    print('Your mark is in Group B.')
elif 60 <= user_mark <= 69:
    print('Your mark is in Group C.')
elif 50 <= user_mark <= 59:
    print('Your mark is in Group D.')
elif 0 <= user_mark <= 49:
    print('Your mark is in Group F.')
else:
    print('Error: The entered mark is not within the valid range (0-100).')
