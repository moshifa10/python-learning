

# This is my First challange to Solve 
# First challange to push in my GitHup

'''
    code challange: 
    You’re given a list of numbers.
    You need to find and print all pairs of numbers that are equal — 
    but make sure you don’t print the same pair twice.
    e.g numbers = [4, 2, 7, 4, 2, 9, 7]
        Output :    (4, 4)
                    (2, 2)
                    (7, 7)

    key: no sets, no count(), only nested loops.
'''


def find_duplicates_pairs(numbers: list) -> tuple:
    tracking = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] == numbers[j] and i != j:
                if (numbers[i], numbers[j]) not in tracking:
                    tracking.append((numbers[i], numbers[j]))
                    print((numbers[i],numbers[j]))

find_duplicates_pairs([4, 2, 7, 4, 2, 9, 7])


# Second challange :
#       Now try to store the duplicates and print them all at once at the end, like:
                            # Duplicate numbers found: [4, 2, 7]
def storing_duplicates(numbers: list) -> tuple:
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i+ 1, len(numbers)):
            if numbers[i] == numbers[j]:
                if numbers[i] not in duplicates:
                    duplicates.append(numbers[i])

    return (f"Duplicates numbers found: {duplicates}")

print(storing_duplicates([4, 2, 7, 4, 2, 9, 7]))
