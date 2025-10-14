

# Challange 17


'''

    🧩 Challenge 17 — “Customer Spending Analyzer”
    1. You are given a list of customer purchases (in rands).
    2. Write a function that analyzes their spending habits.
    Example:
        Input:
            purchases = [120, 130, 140, 110, 115, 125, 150, 160, 120]
        Output:
            {
                "highest_purchase": 160,
                "lowest_purchase": 110,
                "average_spending": 130.0,
                "consistent_spender": False,
                "increasing_streak": 4
            }
'''

def analyze_spending(purchases: list[int]) -> dict:
    save_streak = 0
    streak = 0
    streak_amount = -1000
    for i in purchases:
        if i > streak_amount:
            streak += 1
            streak_amount = i
        else:
            if streak > save_streak:
                save_streak = streak
            streak = 0
            streak_amount = i
        if streak> save_streak:
            save_streak =  streak

    print(((max(purchases)-min(purchases))/max(purchases)) * 100)
    print( max(purchases)*0.2)
    return {
        "highest_purchase": max(purchases),
        "lowest_purchase": min(purchases),
        "average_spending": round(sum(purchases)/ len(purchases)),
        "consistent_spender": ((max(purchases)-min(purchases))/max(purchases)) * 100 < max(purchases)*0.2  ,
        "increasing_streak": save_streak
    }

# print(analyze_spending([120, 130, 140, 110, 115, 125, 150, 160, 120]))
print(analyze_spending([115, 125, 150, 160]))