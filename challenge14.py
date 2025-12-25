

# Challange 14 


'''
💼 Challenge 14: Employee Performance Analyzer
🧠 Scenario 
    1. You’re given a list of employee records.
    2. Each record is a dictionary containing:
        - "name" — employee name
        - "department" — the department they work in
        - "sales" — the total sales amount they made
    Your goal: analyze the data and find out who’s performing best.

    Example:
        Input: 
            employees = [
                {"name": "Alice", "department": "Electronics", "sales": 12000},
                {"name": "Bob", "department": "Clothing", "sales": 8000},
                {"name": "Charlie", "department": "Electronics", "sales": 15000},
                {"name": "Dana", "department": "Clothing", "sales": 7000},
                {"name": "Njabulo", "department": "Home", "sales": 11000}
            ]
        Output:
                {
                "total_sales_per_department": {
                    "Electronics": 27000,
                    "Clothing": 15000,
                    "Home": 11000
                },
                "top_seller": "Charlie",
                "top_seller_sales": 15000,
                "average_sales": 10600.0,
                "department_with_highest_sales": "Electronics"
                }

    🧩 Bonus Challenge (optional)
        Add a new key:
            "ranked_employees": [("Charlie", 15000), ("Alice", 12000), ("Njabulo", 11000), .
'''

def analyze_employees(employees: list[dict]) -> dict:
    departments_sales = {}
    top_seller = ""
    top_seller_sales = 0 
    all_sales = []
    for i in employees:
        name,department,sales = i["name"], i["department"], i["sales"]
        if department not in departments_sales.keys():
            departments_sales[department] = sales
        else:
            departments_sales[department] += sales
        if sales > top_seller_sales:
            top_seller = name
            top_seller_sales = sales
        all_sales.append(sales)
    department_with_highest_sales = max(departments_sales, key=departments_sales.get)
    return {
        "total_sales_per_department": departments_sales,
        "top_seller": top_seller,
        "top_seller_sales": top_seller_sales,
        "average_sales": sum(all_sales) / len(all_sales),
        "department_with_highest_sales": department_with_highest_sales
    }

employees = [
    {"name": "Alice", "department": "Electronics", "sales": 12000},
    {"name": "Bob", "department": "Clothing", "sales": 8000},
    {"name": "Charlie", "department": "Electronics", "sales": 15000},
    {"name": "Dana", "department": "Clothing", "sales": 7000},
    {"name": "Njabulo", "department": "Home", "sales": 11000}
]
print(analyze_employees(employees))