"""
Filter countries containing 'land' in their names.

This script imports a list of countries from the 'countries' module
and creates a new list containing only the countries with 'land' in their names.
"""

import countries

# Initialize an empty list to store countries with 'land' in their names
countries_with_land = []

# Iterate through the list of countries
for country_name in countries.countries:
    # Check if 'land' is in the country name
    if 'land' in country_name.lower():
        countries_with_land.append(country_name)

# Print the list of countries containing 'land'
print("Countries containing 'land' in their names:")
print(countries_with_land)
