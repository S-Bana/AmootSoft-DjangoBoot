from countries_data import countries_data

def count_top_ten_languages(countries_data):
    """
    Count and print the top ten most spoken languages from the given countries data.

    Args:
    countries_data (list): A list of dictionaries containing country information.

    Returns:
    None: Prints the top ten languages and their counts.
    """
    # Create a list of all languages
    all_languages = []
    for country in countries_data:
        all_languages.extend(country["languages"])
    
    # Get unique languages
    unique_languages = set(all_languages)
        
    # Count occurrences of each language
    language_counts = {}
    for language in unique_languages:
        language_counts[language] = all_languages.count(language)
    
    # Find and print top ten languages
    top_ten_languages = {}
    for _ in range(10):
        if not language_counts:
            break
        max_count = max(language_counts.values())
        for language, count in language_counts.items():
            if count == max_count:
                top_ten_languages[language] = count
                del language_counts[language]
                print(f"{language}: {count}")
                break

# Usage
count_top_ten_languages(countries_data)

# ========================================================================================


def find_most_populous_countries(countries_data):
    """
    Find and print the ten most populous countries from the given data.

    Args:
    countries_data (list): A list of dictionaries containing country information.
                           Each dictionary should have 'name' and 'population' keys.

    Returns:
    None: This function prints the results and doesn't return any value.
    """
    # Create a dictionary of country names and their populations
    country_populations = {}
    for country in countries_data:
            country_populations[country["name"]]=country["population"]

    # Find and print top ten most populous countries
    top_ten_countries = {}
    for _ in range(10):
        max_population = max(country_populations.values())
        for country, population in country_populations.items():
            if population == max_population:
                top_ten_countries[country] = population
                country_populations.pop(country)
                print(f"{country}: {population}")
                break 

# Usage
find_most_populous_countries(countries_data)
