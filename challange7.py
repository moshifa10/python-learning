

# Challenge 7: “Smart Filter”


'''
    CHALLANGE 7 : SMART FILTER
    Goal: Write a function that filters and formats mixed data based on type and rules.
    1. Write a function named smart_filter(data) that:
    2. Accepts a list called data containing integers, floats, and strings.
    3. Returns a dictionary with three keys:
        - "numbers" → a list of all numbers (integers or floats) greater than 10.
        - "words" → a list of all strings longer than 4 characters.
        - "formatted" → a list of all strings from "words" converted to uppercase and all numbers from "numbers" converted to strings.

    EXAMPLE:
        Input:
           data = [4, 15, "cat", "python", 7.5, "code", 11.2, "openai"] 
        Output: 
            {
                "numbers": [15, 11.2],
                "words": ["python", "openai"],
                "formatted": ["15", "11.2", "PYTHON", "OPENAI"]
            }
'''

def smart_filter(data: list , min_length=6 ) -> dict:
    filtered = {}
    numbers = []
    word = []
    for i in data:
        if isinstance(i, str) and len(i) > 4:
            word.append(i)
        elif (isinstance(i, int)  or isinstance(i, float)) and i > 10:
            numbers.append(i)
    filtered["numbers"] = numbers
    filtered["words"] = word
    filtered["formatted"] = [str(n) for n in numbers] + [i.upper() for i in word] 

    print(filtered)
    return filtered

data = [4, 15, "cat", "python", 7.5, "code", 11.2, "openai"]
smart_filter(data)

     