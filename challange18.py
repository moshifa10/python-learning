


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
    # print(average_water)

    for i in data:
        for j in i:
            if j not in average.keys():
                average[j] = i[j]
            else:
                average[j] += i[j]

    print(average)

            
    return {
        "average": ...,
        "highest_usage_day": ...,
        "longest_warming_streak": ...,
        "energy_efficient": ...,
        "weather_pattern": ...,
        "city_score": ...,
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