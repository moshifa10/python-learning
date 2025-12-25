


# Challange 15: Data trends analyzer

'''

🧠 Challenge 15: Data Trends Analyzer

1. You’re given a list of sales numbers for each month of a store.
2. Your task is to analyze the data and output:
        1️⃣ The average sales.
        2️⃣ The highest month (month number and value).
        3️⃣ The longest increasing streak of months.
        4️⃣ Whether sales ever dropped below zero.
    Example:
        Input:
            sales = [1200, 1500, 1700, 1600, 1800, 2000, 2100, 1900, 2300, 2500, 2400, 2600]
        Output:
            {
                "average": 1966.67,
                "highest_month": (12, 2600),
                "longest_increase_streak": 3,
                "has_negative": False
            }

'''

def analyze_sales(sales: list[int]) -> dict:
    highest_month = max(sales)
    has_negative = False
    longest_increasing = sales[0]
    count_longest = 1
    dict_longest_count ={}
    for i in sales:
        if i < 0:
            has_negative = True
    for count,i in enumerate(sales):
        if i > longest_increasing:
            longest_increasing = i
            count_longest += 1
            if count+1 ==len(sales):
                dict_longest_count[count_longest] = longest_increasing
            
        else:
            dict_longest_count[count_longest]= longest_increasing
            longest_increasing = i
            count_longest = 1 
        

    return {
        "average": round(sum(sales) / len(sales), 2),
        "highest_month": (sales.index(highest_month) + 1, highest_month),
        "longest_increasing_streak": max(dict_longest_count.keys()),
        "has_negative": has_negative
    }

# print(analyze_sales([1200, 1500, 1700, 1600, 1800, 2000, 2100, 1900, 2300, 2500, 2400, 2600]))
# print(analyze_sales( [1000, 1200, 1300, 1100, 1150, 1170, 1190, 1210, 1180, 1250, 1270, 1290]))
# print(analyze_sales( [1000, 1200, 1300, 900, 1100, 1200]))
# print(analyze_sales( [1000, 1200, 1100, 1150, 1300, 900, 950]))
print(analyze_sales( [100, 200, 300]))
