

# Challange 16

'''

🧩 Challenge 16 — "Temperature Tracker"

1. You are given a list of daily temperatures recorded over several days.
2. You must analyze the data and return these results:

    - 🧠 Your function must return a dictionary containing:
        1. "longest_warming_streak" — the number of consecutive days where the temperature increased.
        2. "coolest_day" — the lowest temperature and its day index (starting at 1).
        3. "average_temperature" — the rounded average of all temperatures.
        4. "temp_fluctuation" — the difference between the highest and lowest temperature.

    Example:
        Input:
            temps = [22, 24, 25, 23, 26, 27, 21, 20, 22, 23, 24]
        Output:
            {
                "longest_warming_streak": 3,
                "coolest_day": (7, 21),
                "average_temperature": 23.36,
                "temp_fluctuation": 7
            }

'''

def temp_tracker(temps: list[int]) -> dict:
    lowest_temp = min(temps)
    highest_temp = max(temps)
    temps_streak = -100
    streak = 0
    current_streak = 1
    for i in range(len(temps)):
        if temps[i] > temps_streak:
            streak += 1
            temps_streak = temps[i]
        else:
            streak = 0
            temps_streak = temps[i]
        if streak > current_streak:
            current_streak = streak

    return {
        "longest_warming_streak": current_streak,
        "coolest_day": (temps.index(lowest_temp) +1,lowest_temp),
        "average_temperature": round(sum(temps)/len(temps), 2),
        "temp_fluctuation": abs(highest_temp-lowest_temp)
    }

# print(temp_tracker(temps = [22, 24, 25, 23, 26, 27, 21, 20, 22, 23, 24]))
print(temp_tracker([22, 24, 23, 25]))