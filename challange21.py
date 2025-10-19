


# Challange 21

'''


💥 Challenge 21: "Business Performance Intelligence"
🧠 Scenario
    You’re building a mini data intelligence system for a company that wants to track:
        1. sales trends
        2. employee performance
        3. product category analysis
        4. and business efficiency
    📊 Data Example
    You’ll be given a list of dictionaries like this:
            business_data = [
                {
                    "month": "January",
                    "sales": [
                        {"employee": "Alice", "category": "Tech", "amount": 1200},
                        {"employee": "Bob", "category": "Home", "amount": 900},
                        {"employee": "Charlie", "category": "Tech", "amount": 1500},
                        {"employee": "Diana", "category": "Garden", "amount": 800}
                    ],
                    "expenses": 1800
                },
                {
                    "month": "February",
                    "sales": [
                        {"employee": "Alice", "category": "Tech", "amount": 1300},
                        {"employee": "Bob", "category": "Home", "amount": 1000},
                        {"employee": "Charlie", "category": "Tech", "amount": 1600},
                        {"employee": "Diana", "category": "Garden", "amount": 850}
                    ],
                    "expenses": 2000
                },
                {
                    "month": "March",
                    "sales": [
                        {"employee": "Alice", "category": "Tech", "amount": 1250},
                        {"employee": "Bob", "category": "Home", "amount": 950},
                        {"employee": "Charlie", "category": "Tech", "amount": 1550},
                        {"employee": "Diana", "category": "Garden", "amount": 900}
                    ],
                    "expenses": 2100
                }
            ]

    Output:
            {
            "monthly_profit": {"January": 2600, "February": 2750, "March": 2650},
            "top_employee": "Charlie",
            "top_category": "Tech",
            "best_month": "February",
            "consistency_score": {"Charlie": 6, "Alice": 5, "Bob": 3, "Diana": 4},
            "overall_efficiency": 1.35,
            "insights": ["Profits are increasing", "Employee consistency improving"]
            }
'''