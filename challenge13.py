

# Challange 13

'''
🎯 Challenge 13: The Guess Analyzer
🧩 Story
    1. Imagine a simple number-guessing game where multiple players guess numbers between 1–10.
    2. You’re given all their guesses, and your job is to analyze who was closest to the secret number.
    Example:
        - guesses is a dictionary of player names and their guesses, e.g.:
        Input:
            {"Alice": 5, "Bob": 9, "Charlie": 3, "Njabulo": 7}
        Output:
            {
            "closest_player": "Njabulo",
            "closest_difference": 1,
            "guesses_above": ["Bob"],
            "guesses_below": ["Alice", "Charlie"],
            "all_differences": {"Alice": 3, "Bob": 1, "Charlie": 5, "Njabulo": 1}
            }
'''

guesses = {"Alice": 5, "Bob": 10, "Charlie": 3, "Njabulo": 7}
def guess_analyzer(guesses: dict, secret: int) -> dict:
    # I can start by getting all guesses differences then get the lowest -> means it's that closest player 
    all_differences = {}
    
    closest = 11
    closest_player = ""
    for key,val in guesses.items():
        all_differences[key] = abs(val- secret)
    above = []
    below = []
    # minimum = min(all_differences.values())
    for key,val in all_differences.items():
        if val < closest :
            closest = val
            closest_player = key
    del guesses[closest_player]
    del all_differences[closest_player]
    all_closest_players = []
    for key,val in all_differences.items():
        if val == closest:
            all_closest_players.append(key)
            del guesses[key]

    for key,value in guesses.items():
        if value > secret:
            above.append(key)
        elif value < secret:
            below.append(key)
    return {
        "closest_player":  all_closest_players +[closest_player],
        "closest_difference": closest,
        "guesses_above": above,
        "guesses_below": below,
        "all_differences": all_differences
    }

print(guess_analyzer(guesses, 8))
