


# Challange 18

'''

⚔️ Challenge 18 — The Smart City Analytics Game
🧠 Background:
    1. You’re managing a futuristic smart city.
    2. The city collects daily data about:
        Energy usage (kWh)
        Water consumption (litres)
        Traffic flow (vehicles/hour)
        Weather temperature (°C)
    Your job is to analyze the data and generate insights for the city report system.

    Example:
        Input:
            data = [
                {"day": 1, "energy": 150, "water": 300, "traffic": 500, "temperature": 20},
                {"day": 2, "energy": 160, "water": 280, "traffic": 520, "temperature": 22},
                {"day": 3, "energy": 155, "water": 310, "traffic": 480, "temperature": 25},
                {"day": 4, "energy": 170, "water": 290, "traffic": 530, "temperature": 27},
                {"day": 5, "energy": 165, "water": 275, "traffic": 510, "temperature": 24},
                {"day": 6, "energy": 180, "water": 320, "traffic": 550, "temperature": 21},
            ]
        Output:
            {
            "average": {"energy": 163.3, "water": 295.8, "traffic": 515.0, "temperature": 23.2},
            "highest_usage_day": 6,
            "longest_warming_streak": 3,
            "energy_efficient": True,
            "weather_pattern": "cooling trend",
            "city_score": 25.8
            }

'''


def smart_city_analyer(data: list[dict]) -> dict:
    average_energy = [i["energy"]for i in data]
    average_water = [i["water"] for i in data]
    average_traffic = [i["traffic"] for i in data]
    average_temp = [i["temperature"] for i in data]
    average = {}
    days= {}
    # print(average_water)

    for i in data:
        for j in i:
            # print(j)
            day, energy, water, traffic, temp = i["day"], i["energy"], i["water"], i["traffic"], i["temperature"]
            days[day]= energy+water+traffic+temp
            if j not in average.keys():
                average[j] = i[j]
            else:
                average[j] += i[j]
    streak = 0
    current = -10000
    save_streak = 0
    droping = 0
    save_droping = 0
    streak_drop = ''
    for i in data:
        day, energy, water, traffic, temp = i["day"], i["energy"], i["water"], i["traffic"], i["temperature"]
        if temp > current:
            streak += 1
            current = temp
        else:
            if streak > save_streak:
                save_streak = streak
                streak = 0
                current = temp
            streak = 0
            current = temp
        if streak > save_streak:
            save_streak = streak
        if temp < current:
            droping += 1
            current = temp
        else:
            if droping > save_droping:
                save_droping = droping
                droping =0
                current = temp
            droping = 0
            current = temp

    if save_streak >= 3:
        streak_drop = "warming trend"
    elif save_droping >= 3:
        streak_drop = "cooling trend"
    else:
        streak_drop = "stable"
    for i in average:
        if i == "energy":
            average[i] /= len(average_energy)
        elif i == "water":
            average[i] /= len(average_water)
        elif i == "traffic":
            average[i] /= len(average_traffic)
        elif i == "temperature":
            average[i] /= len(average_temp)

    for i in average:
        average[i] = round(average[i],1)
    # print(max([i["temperature"] for i in data]))
    # city_score (avg_temp / max_temp * 20) + (efficiency * 10)  
    efficiency = average["energy"] < max([i["temperature"] for i in data]) * 0.8
    if efficiency:
        efficiency = 1
    else: efficiency = 0
    arr = [-3, 5, 16, -7, -1, -1, 644, -923, 93, -682, -923, 10, 128, 657, -88]
    print([len([i for i in range(len(arr)) if arr[i] > 0]), sum([b for b in arr if b < 0])])
    print(sum([i for i in arr if max(arr) != i and min(arr) != i]))
    return {
        "average": average,
        "highest_usage_day": max(days, key=days.get),
        "longest_warming_streak": save_streak,
        "energy_efficient": average["energy"] < max([i["energy"] for i in data]) * 0.8,
        "weather_pattern": streak_drop,
        "city_score": round((average["temperature"] / max([i["temperature"] for i in data]) * 20) + (efficiency * 10),2),
    }



data = [

    {"day": 1, "energy": 150, "water": 300, "traffic": 500, "temperature": 20},
    {"day": 2, "energy": 160, "water": 280, "traffic": 520, "temperature": 22},
    {"day": 3, "energy": 155, "water": 310, "traffic": 480, "temperature": 25},
    {"day": 4, "energy": 170, "water": 290, "traffic": 530, "temperature": 27},
    {"day": 5, "energy": 165, "water": 275, "traffic": 510, "temperature": 24},
    {"day": 6, "energy": 180, "water": 320, "traffic": 550, "temperature": 21},
]
print(smart_city_analyer(data))