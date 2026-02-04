''''

    Challange 23 


    📘 README
Student Intelligence & Risk Analytics Engine

Challenge 23 Specification

🧠 Project Overview:
    This project focuses on advanced student data analysis using pure Python data structures.
    The goal is to simulate how real analytics systems reason about performance, consistency, engagement, and risk — without using any external libraries or frameworks.

You will analyze structured student data and produce insightful, explainable results.
    🚫 Restrictions:
        ❌ No pandas
        ❌ No numpy
        ❌ No argparse
        ❌ No CSV reading
        ❌ No external libraries
    ✅ Allowed:
        Lists
        Dictionaries
        Loops
        Conditionals
        Built-in functions
        Logical reasoning

📥 Input Data Structure
You are given a list of dictionaries, where each dictionary represents a student.
Each student contains:
    - A name
    - A history of scores
    - Attendance records
    - Participation scores
    - Late submissions
    - Optional extra credit data
    ⚠️ Data may be uneven or incomplete, and your logic must handle this safely.

🎯 Objectives & Required Analyses:
    1️⃣ Normalized Student Averages

    What to do
    - Compute an adjusted average score per student.
    - Ignore the lowest score.
    - Give more weight to recent tests.
    Why
    - Simulates real-world grading systems.
    - Tests indexing, slicing, and weighting logic.
    Expected Output Format
        {
        "Alice": 84.6,
        "Bob": 68.2,
        "Charlie": 91.4,
        "Diana": 71.0
        }

2️⃣ Class Stability Index
    What to do
        - Measure how stable the class is overall.
        - Based on how far student averages differ from one another.

    Why
        - Evaluates class-wide performance balance.

    Expected Output Format
        82.35

3️⃣ Consistency Score & Label
    What to do
        - Assign a numeric consistency score per student.
        - Convert the score into a label:
        - Highly Consistent
        - Moderate
        - Unstable

    Why
        - Measures reliability, not performance.
    Expected Output Format:
        {
        "scores": {
            "Alice": 6,
            "Bob": 3,
            "Charlie": 7,
            "Diana": 4
        },
        "labels": {
            "Alice": "Moderate",
            "Bob": "Unstable",
            "Charlie": "Highly Consistent",
            "Diana": "Moderate"
        }

    }

4️⃣ Trend Classification
    What to do
        Classify each student as one of:
            - Improving
            - Declining
            - Volatile
            - Plateaued

        Why
        - Tests pattern recognition over time.

        Expected Output Format:
            {
            "Alice": "Improving",
            "Bob": "Volatile",
            "Charlie": "Plateaued",
            "Diana": "Declining"
            }

5️⃣ Engagement Momentum
    What to do
        Determine whether engagement is trending:
            - Positive
            - Neutral
            - Negative

        Why
        - Introduces temporal reasoning.

        Expected Output Format
            {
            "Alice": "Positive",
            "Bob": "Neutral",
            "Charlie": "Positive",
            "Diana": "Negative"
            }

6️⃣ Fairness Adjustment
    What to do
        - Adjust engagement scores using fairness logic.
        - Reward effort and penalize disengagement.   

    Why
        - Simulates ethical analytics decisions.

    Expected Output Format
        {
        "Alice": 87.2,
        "Bob": 69.5,
        "Charlie": 92.1,
        "Diana": 65.8
        }

7️⃣ Risk Tier Assignment

What to do
    Assign each student exactly one tier:
        Critical Risk
        High Risk
        Medium Risk
        Safe

    Why
        Tests multi-condition decision logic.

    Expected Output Format
        {
        "Alice": "Safe",
        "Bob": "High Risk",
        "Charlie": "Safe",
        "Diana": "Critical Risk"
        }

8️⃣ Intervention Recommendations
    What to do
    Recommend actions for non-safe students.
        Based on their risk factors.

    Why
        Translates data into real-world decisions.

    Expected Output Format
        {
        "Bob": "Academic tutoring and attendance monitoring",
        "Diana": "Immediate intervention and parent meeting"
        }

9️⃣ Top 3 Student Rankings
    What to do
    Rank students by final adjusted engagement score.
        Handle ties gracefully.

    Expected Output Format
        ["Charlie", "Alice", "Bob"]

🔁 10️⃣ Consistency vs Improvement Paradox

What to do

Identify students who are consistent but not improving.

Explain why using data-driven reasoning.

Expected Output Format

{
  "Alice": "Scores stable but no upward trend",
  "Charlie": "High consistency with minimal variation"
}

📦 Final Output Structure

Your function must return one dictionary:

{
  "normalized_averages": {...},
  "class_stability_index": float,
  "consistency": {...},
  "trend_classification": {...},
  "engagement_momentum": {...},
  "adjusted_engagement_scores": {...},
  "risk_tiers": {...},
  "intervention_plan": {...},
  "top_3_students": [...],
  "consistency_improvement_paradox": {...}
}

'''
def measure_reliability(data: dict) -> dict:

    '''- Highly Consistent
        - Moderate
        - Unstable
    '''

    for student, score_list in data.items():
        consistency =  0
        keep = 0
        all_scrores = {}
        for score in score_list:
            if score > consistency:
                consistency += 1
            elif score < consistency:
                if consistency> keep:
                    keep = consistency
                    consistency = 0
                else:
                    consistency= 0
        all_scrores[student] = consistency

        
        
            



def calculate_stability(data: dict) -> float:
    avarages =list(map(float, [value for key, value in data.items()]))
    return float(f"{(sum(avarages) / len(avarages)):.2f}")

def analyse_student(data: list[dict]) -> dict: 
    avarages = {key["name"]: float(f"{sum(key["scores"])/len(key["scores"]):.2f}") for key in data}   
    scores = {dic.get("name", []):dic.get("scores", []) for dic in data}
    stability = calculate_stability(avarages)

    # print(avarages)   

    return{
        "normalized_averages" : avarages,
        "class_stability_index": stability,
        "consistency": ...

    }


students = [
    {
        "name": "Alice",
        "scores": [72, 78, 81, 85, 88],
        "attendance": [1, 1, 1, 0, 1],
        "participation": [6, 7, 7, 8, 9],
        "late_submissions": [0, 1, 0, 0, 0],
        "extra_credit": [2, 3]
    },
    {
        "name": "Bob",
        "scores": [65, 60, 58, 62, 59],
        "attendance": [1, 0, 1, 1, 0],
        "participation": [5, 4, 4, 5, 4],
        "late_submissions": [1, 1, 1, 0, 1],
        "extra_credit": []
    },
    {
        "name": "Charlie",
        "scores": [88, 90, 92, 94, 93],
        "attendance": [1, 1, 1, 1, 1],
        "participation": [8, 8, 9, 9, 9],
        "late_submissions": [0, 0, 0, 0, 0],
        "extra_credit": [5]
    },
    {
        "name": "Diana",
        "scores": [70, 68, 65, 60],
        "attendance": [1, 1, 0, 0],
        "participation": [6, 6, 5, 5],
        "late_submissions": [0, 1, 1, 1],
        "extra_credit": []
    },
    {
        "name": "Ethan",
        "scores": [55, 60, 58],
        "attendance": [0, 1, 1],
        "participation": [4, 5, 5],
        "late_submissions": [1, 0, 1],
        "extra_credit": [1, 2, 1]
    }
]

print(analyse_student(students))