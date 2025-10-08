import json

# CHALLANGE 8 

'''
    Challange 8: Student Performance Analyzer
    Goal: Work with nested data structures (lists + dicts) and perform data processing like a real-world system.
    Write a function called analyze_students(students: list) that:
    1. Accepts a list of student records
    2. Returns a dictionary with:
        "average_scores" → a dictionary mapping each student’s name to their average score (rounded to 2 decimals).
        "top_student" → the name of the student with the highest average.
        "failed_students" → a list of student names whose average < 50.
        "overall_average" → the average of all students’ averages (rounded to 2 decimals).
    
    Examples: 
        INPUT:
            students = [
            {"name": "Alice", "scores": [80, 90, 70], "age": 20},
            {"name": "Bob", "scores": [45, 30, 55], "age": 19},
            {"name": "Charlie", "scores": [60, 75, 65], "age": 21},
            ]
        OUTPUT:
           {
            "average_scores": {"Alice": 80.0, "Bob": 43.33, "Charlie": 66.67},
            "top_student": "Alice",
            "failed_students": ["Bob"],
            "overall_average": 63.33
            } 

        💥 Bonus challenge (for max difficulty)
            Add a keyword argument passing_score=50 so the failure threshold can change dynamically:
'''

def analyze_students(students: list) -> dict:
    performance = {}
    average_scores = {}
    # First is to loop through the list and go row by row
    for each in students:
        for student in each:
            name = each["name"]
            score = each["scores"]
            calc_score = round(sum(score) / (len(score)), 2)
            average_scores[name] = calc_score
    # performance.update({"average_scores",avarage_scores})
    performance["average_scores"] = average_scores
    
    top_student = 0
    name_top_student = ""
    failed_students = []
    overall = 0
    for i in average_scores:
        if average_scores[i] > top_student:
            top_student = average_scores[i]
            name_top_student = i
        if average_scores[i] < 50:
            failed_students.append(i)
        overall += average_scores[i]

    overrall = round(overall / len(average_scores), 2)
    performance["top_student"] = name_top_student
    performance["failed_students"] = failed_students
    performance["overall_average"] = overall
    # json_output = json.dumps(performance, indent=4)
    # print(json_output)
    print(performance)
    return performance
# students = [
#     {"name": "Alice", "scores": [80, 90, 70], "age": 20},
#     {"name": "Bob", "scores": [45, 30, 55], "age": 19},
#     {"name": "Charlie", "scores": [60, 75, 65], "age": 21},
# ]
students = [
    {"name": "Alice", "scores": [80, 90, 70], "age": 20},
    {"name": "Bob", "scores": [45, 30, 55], "age": 19},
    {"name": "Charlie", "scores": [60, 75, 65], "age": 21},
    {"name": "Diana", "scores": [95, 85, 100], "age": 22},
    {"name": "Ethan", "scores": [40, 42, 38], "age": 20}
]
analyze_students(students)
# names = [
#     {"name": "najbu" , "age": 9},
#     {"name": "maj" , "age": 15}
# ]

# for i in names:
#     for j in i:
#         print(i[j])