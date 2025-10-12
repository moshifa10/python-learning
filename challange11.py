

# Challange 11

'''
    🧩 Challenge 11: Number Maze Solver
    🎯 Goal:
        1. You are given a list of integers. Some numbers are “blocked” (negative), and some are “open” (positive).
        2. You need to find the longest consecutive sequence of positive numbers — basically the “longest open path” in the maze.
    It should:
        1. Accept a list of integers (positive and negative).
        2. Return a tuple:
            - The length of the longest consecutive positive sequence
            - The actual sequence itself
    Example:
        Input:
            numbers = [1, 2, -1, 3, 4, 5, -2, 6, 7, 8, 9, -3, 10]
        Output:
            (4, [6, 7, 8, 9])
'''


def longest_open_path(numbers: list[int]) -> tuple[int, list[int]]:
    indexes = []
    streak = 0
    path = {}
    for i in range(len(numbers)):
        # if str(numbers[i]).startswith("-"):
        if numbers[i] < 0:
            path[streak] = indexes
            indexes = []
            streak = 0

        else:
            streak += 1
            indexes.append(numbers[i])

    if streak > 0:
        path[streak] = indexes
    maximum = max(path.keys())
    return (maximum, path[maximum])
            
# print(longest_open_path([1, 2, -1, 3, 4, 5, -2, 6, 7, 8, 9, -3, 10]))
print(longest_open_path([4, -5, 7, 0, 12, -8, 3, 9, -2, 15, 6, -10, 11]))
print(longest_open_path([-1,-2,3]))


        # if str(numbers[i]).startswith("-"):
        #     indexes = []
        # else:
        #     indexes.append(numbers[i])
        #     streak += 1
        #     if len(numbers)-i > 2:...
        #     if str(numbers[i+1]).startswith("-") or (numbers[i+1] == len(numbers) or numbers[i+1] > len(numbers)):
        #         return (streak, indexes)