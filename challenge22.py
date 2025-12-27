

# Challange 22


'''
Challenge 22: Student Performance Insight Engine

You are given a dataset of students, their test scores over time, attendance records, and participation points.Docstring for challenge22

E.G

students = [
    {
        "name": "Alice",
        "scores": [78, 82, 85, 90],
        "attendance": [1, 1, 1, 0],
        "participation": [6, 7, 8, 9]
    },
    {
        "name": "Bob",
        "scores": [65, 60, 58, 62],
        "attendance": [1, 0, 1, 1],
        "participation": [5, 4, 4, 5]
    },
    {
        "name": "Charlie",
        "scores": [88, 90, 92, 94],
        "attendance": [1, 1, 1, 1],
        "participation": [8, 8, 9, 9]
    },
    {
        "name": "Diana",
        "scores": [70, 75, 73, 68],
        "attendance": [1, 1, 0, 0],
        "participation": [6, 6, 5, 5]
    }
]

Output with Explanation

📊 REQUIRED OUTPUT KEYS
    1 Student Averages
        - Compute each student’s average score.
        - Store them in a dictionary.

    2 Class Average
        - Average of all student averages (rounded to 2 decimals).

    3 Consistency Score (you design this!)
        - Lower variation → higher consistency.
        - Use only things you’ve learned.
        - Output example:
            {"Alice": 5, "Bob": 8, "Charlie": 3, "Diana": 6}

    4 Improvement Detection
        - A student is improving if they improve at least twice in a row.
        - Return a list of improving student names.

    5 Attendance Risk
        - Attendance list contains 1 = present, 0 = absent.
        - If attendance rate < 75%, student is at risk.
        - Return list of names.

    6 Engagement Score (NEW CONCEPT 🔥)
        - Create a formula combining:
            average score
            attendance percentage
            participation average
            You design the formula.

    7 Top Performer
        Student with highest engagement score.

    8 Needs Immediate Attention
        A student qualifies if:
            average score < 70 OR
            attendance < 50%

📦 Final Return Format
{
    "student_averages": {...},
    "class_average": float,
    "consistency_score": {...},
    "improving_students": [...],
    "attendance_risk": [...],
    "engagement_scores": {...},
    "top_performer": str,
    "needs_attention": [...]
}



'''

def calculate_consistency(scores: list[int]) -> int:
    '''
    Docstring for calculate_consistency
    In this fun I am calc the consistency and I am thinking of starting from 10 and 
    check the score if is greater: 
        do something ...
        meaning if constant variable is < 10 then increment depending on how big the score increased 
        if score is still 10 just continue
    check the score if less than : 
        do something ...
    '''
    constant = 10

    current = scores[0]
    for i in range(1, len(scores)):
        if scores[i] < current : 
            if not constant == 0:
                difference  =  current - scores[i] 
                if difference > 0 and difference <= 10:
                    constant -= 1
                elif difference > 10 and difference <= 20:
                    constant -= 2
                elif difference > 20 and difference <= 30:
                    constant -= 3
                elif difference > 30 and difference <= 40:
                    constant -= 4
                elif difference > 40 and difference <= 50:
                    constant -= 5
                elif difference > 50 and difference <= 60:
                    constant -= 6 
                elif difference > 60 and difference <= 70:
                    constant -= 7
                elif difference > 70 and difference <= 80:
                    constant -= 8 
                elif difference > 80 and difference <= 90:
                    constant -= 9
                else:
                    constant -= 10

                if constant < 0:
                    constant = 0
        elif scores[i] > current:
            if not constant == 10:
                difference  =  scores[i] - current
                if difference > 0 and difference <= 10:
                    constant += 1
                elif difference > 10 and difference <= 20:
                    constant += 2
                elif difference > 20 and difference <= 30:
                    constant += 3
                elif difference > 30 and difference <= 40:
                    constant += 4
                elif difference > 40 and difference <= 50:
                    constant += 5
                elif difference > 50 and difference <= 60:
                    constant += 6 
                elif difference > 60 and difference <= 70:
                    constant += 7
                elif difference > 70 and difference <= 80:
                    constant += 8 
                elif difference > 80 and difference <= 90:
                    constant += 9
                else:
                    constant += 10

                if constant > 10:
                    constant = 10
            current = scores[i]
    return constant 

def calculate_engagement_scores(average_score: float, attendance_percentage: int, participation_average: float) -> int:
    '''
    In this func It will be engagement_score :
        It will take some scores from the student and combine them to make a score
        This will determine if a student was more engaged 
    '''
    # return int((((average_score/100) + (attendance_percentage/100) + ((participation_average*100)/100)/ 300))*100)
    return f"{((average_score + attendance_percentage + (participation_average * 10))/300) * 100:.2f}"




def insight_engine(students: list[dict]) -> dict:
    students_average = {}
    consistency = {}
    improving_students = []
    attendance_list = []
    engagement_scores = {}
    students_at_risk = []
    for each in students:
        name, scores, attendance, participation = each['name'], each['scores'], each['attendance'], each['participation']
        average_score = sum(scores)/len(scores)
        students_average[name] = average_score
        
        #------------------ here I will calculate the consistency --------------
        constant = calculate_consistency(scores)
        consistency[name] = constant

        #--------------- Here I will be calculating improving students --------------
        start = scores[0]
        improve = 0
        store = 0
        for score in scores:
            if score > start:
                improve +=1 
                start = score
            elif score < start:
                store = improve
                improve = 0

        if store > 1 or improve > 1:
            improving_students.append(name)
        
        # ----------------    Here I will be calculating attendance risk      ----------------
        attendance_percentage = round((sum(attendance) / len(attendance))* 100)
        calc_risk = True if  attendance_percentage >= 75 else False
        if not calc_risk:
            attendance_list.append(name)


        # ------------  Here I will be calculating engagement score ----------
        participation_average = (sum(participation)/len(participation))
        calculations_engagement = calculate_engagement_scores(average_score, attendance_percentage, participation_average)
        engagement_scores[name]= calculations_engagement    
        
        # ------------ Here I will be calculating the students at risk ------------
        if attendance_percentage < 50 or average_score < 75:
            students_at_risk.append(name)

    return {
        "student_averages": students_average,
        "class_average": round(sum([marks for student, marks in students_average.items()])/ len(students_average),2),
        "consistency_score": consistency,
        "improving_students": improving_students,
        "attendance_risk": attendance_list,
        "engagement_scores": list(engagement_scores.values()),
        "top_performer": max(engagement_scores, key=engagement_scores.get),
        "needs_attention": students_at_risk
    }




students = [
    {
        "name": "Alice",
        "scores": [78, 82, 85, 90],
        "attendance": [1, 1, 1, 0],
        "participation": [6, 7, 8, 9]
    },
    {
        "name": "Bob",
        "scores": [65, 60, 58, 62],
        "attendance": [1, 0, 1, 1],
        "participation": [5, 4, 4, 5]
    },
    {
        "name": "Charlie",
        "scores": [88, 90, 92, 94],
        "attendance": [1, 1, 1, 1],
        "participation": [8, 8, 9, 9]
    },
    {
        "name": "Diana",
        "scores": [70,45 , 30, 7],
        "attendance": [1, 1, 0, 0],
        "participation": [6, 6, 5, 5]
    }
]

print(insight_engine(students))