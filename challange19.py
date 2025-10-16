

# challange 19

'''

.

🧠 Challenge 19: “Student Performance Analyzer”
1. You are given a list of dictionaries, where each dictionary represents a student and their test scores.

    Example: 
        Input:
            students = [
                {"name": "Alice", "scores": [80, 85, 88, 90]},
                {"name": "Bob", "scores": [70, 68, 72, 75]},
                {"name": "Charlie", "scores": [90, 95, 92, 93]},
                {"name": "Diana", "scores": [60, 65, 62, 58]}
            ]
        Output:

            {
                "top_student": ("Charlie", 92.5),
                "lowest_student": ("Diana", 61.25),
                "class_average": 77.94,
                "improving_students": ["Alice", "Bob"],
                "needs_attention": ["Diana"]
            }
'''

def performance_analyzer(students :list[dict]) -> dict:
    # students = students[0]
    top = 0
    name_ = ''
    for i in students:
        name, scores = i["name"], i["scores"]
        if top == 0:
            top = sum(scores)
            name_ = name
        else:
            topping = max(sum(scores),top)
            if topping == sum(scores):
                top = topping
                name_ = name
    print((name_, top))


    return{
        "top_student": name
    }


students = [
    {"name": "Alice", "scores": [80, 85, 88, 90]},
    {"name": "Bob", "scores": [70, 68, 72, 75]},
    {"name": "Charlie", "scores": [90, 95, 92, 93]},
    {"name": "Diana", "scores": [60, 65, 62, 58]}
]


performance_analyzer(students)