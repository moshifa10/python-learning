📘 README
Student Intelligence & Risk Analytics Engine

Challenge 23 Specification

🧠 Project Overview

This project focuses on advanced student data analysis using pure Python data structures.
The goal is to simulate how real analytics systems reason about performance, consistency, engagement, and risk — without using any external libraries or frameworks.

You will analyze structured student data and produce insightful, explainable results.

🚫 Restrictions

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

A name

A history of scores

Attendance records

Participation scores

Late submissions

Optional extra credit data

⚠️ Data may be uneven or incomplete, and your logic must handle this safely.

🎯 Objectives & Required Analyses
1️⃣ Normalized Student Averages

What to do

Compute an adjusted average score per student.

Ignore the lowest score.

Give more weight to recent tests.

Why

Simulates real-world grading systems.

Tests indexing, slicing, and weighting logic.

Expected Output Format

{
  "Alice": 84.6,
  "Bob": 68.2,
  "Charlie": 91.4,
  "Diana": 71.0
}

2️⃣ Class Stability Index

What to do

Measure how stable the class is overall.

Based on how far student averages differ from one another.

Why

Evaluates class-wide performance balance.

Expected Output Format

82.35

3️⃣ Consistency Score & Label

What to do

Assign a numeric consistency score per student.

Convert the score into a label:

Highly Consistent

Moderate

Unstable

Why

Measures reliability, not performance.

Expected Output Format

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

Improving

Declining

Volatile

Plateaued

Why

Tests pattern recognition over time.

Expected Output Format

{
  "Alice": "Improving",
  "Bob": "Volatile",
  "Charlie": "Plateaued",
  "Diana": "Declining"
}

5️⃣ Engagement Momentum

What to do

Determine whether engagement is trending:

Positive

Neutral

Negative

Why

Introduces temporal reasoning.

Expected Output Format

{
  "Alice": "Positive",
  "Bob": "Neutral",
  "Charlie": "Positive",
  "Diana": "Negative"
}

6️⃣ Fairness Adjustment

What to do

Adjust engagement scores using fairness logic.

Reward effort and penalize disengagement.

Why

Simulates ethical analytics decisions.

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