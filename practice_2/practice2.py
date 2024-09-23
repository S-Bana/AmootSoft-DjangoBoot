# Create a tournament bracket system

import random

def random_pairing(teams):
    """Randomly pairs teams and removes one team from each pair."""
    random.shuffle(teams)  # Shuffle the teams to ensure random pairing
    
    pairs = []
    while len(teams) > 1:
        team1 = teams.pop()  # Remove the last team from the list
        team2 = teams.pop()  # Remove the second last team from the list
        pairs.append((team1, team2))  # Create a pair and add to pairs list
    
    return pairs

def eliminate_teams(pairs):
    """Removes one team from each pair and returns the winners."""
    winners = []
    for team1, team2 in pairs:
        winner = random.choice([team1, team2])  # Randomly choose a winner from each pair
        winners.append(winner)  # Add the winner to the winners list
    return winners

def determine_winner(teams):
    """Recursively determines the overall winner."""
    if len(teams) == 1:  # Base case: if only one team remains
        return teams[0]  # Return that team as the winner
    
    pairs = random_pairing(teams)  # Create pairs for the current round
    print("Pairs for this round:")
    for team1, team2 in pairs:
        print(f"{team1} vs {team2}")  # Print the pairs
    
    winners = eliminate_teams(pairs)  # Eliminate teams and get winners
    print("Winners of this round:")
    for winner in winners:
        print(winner)  # Print the winners of the round
    
    print()  # Print a blank line for better readability
    return determine_winner(winners)  # Recursively determine the winner from the winners

def play():
    # Input: List of teams
    teams = input("Enter the list of teams separated by commas: ").split(',')
    teams = [team.strip() for team in teams]  # Clean up whitespace

    # Ensure there are enough teams to form pairs
    if len(teams) < 2:
        print("At least two teams are required to form pairs.")
        return
    
    winner = determine_winner(teams)  # Determine the overall winner
    print(f"The overall winner is: {winner}")

play()