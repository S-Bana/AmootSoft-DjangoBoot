"""
This Python script defines a dictionary containing personal information about an individual,
including their name, age, country, marital status, skills, and address. It performs the following actions:

1. Checks if the 'skills' key exists in the dictionary and prints the first skill, last skill,
   and the middle skill from the list of skills.
   
2. Checks if 'Python' is one of the skills listed for the individual and prints 'true' if it is,
   or 'false' if it is not.
   
3. Prints a formatted string that includes the person's full name, country of residence,
   marital status, and a list of their skills.
"""

# Define a dictionary to store a person's information
person_info = {
    'first_name': 'Ehsan',  # Person's first name
    'last_name': 'Hosseini',  # Person's last name
    'age': 250,  # Person's age
    'country': 'Iran',  # Person's country of residence
    'is_married': True,  # Marital status of the person
    'skills': ['JavaScript', 'Django', 'Odoo', 'MongoDB', 'Python'],  # List of skills the person has
    'address': {  # Dictionary to store the person's address
        'street': 'Space street',  # Street name
        'postal_code': '02210'  # Postal code
    }
}

# Check if the 'skills' key exists in the person_info dictionary
if 'skills' in person_info:
    # Print the first skill, last skill, and the middle skill from the skills list
    print(person_info['skills'][0], person_info['skills'][-1], person_info['skills'][len(person_info['skills']) // 2])

# Check if 'Python' is in the skills list
if 'Python' in person_info['skills']:
    print('true')  # Print 'true' if Python is in the skills list
else:
    print('false')  # Print 'false' if Python is not in the skills list

# Print a formatted string with the person's information
print(f"{person_info['first_name']} {person_info['last_name']} lives in {person_info['country']}. They are {'married' if person_info['is_married'] else 'not married'}. They have these skills: {', '.join(person_info['skills'])}")
