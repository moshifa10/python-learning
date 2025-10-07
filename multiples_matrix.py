


# Challange 3 

'''
    Challange 3: Multiples Matrix
    1. You are given a list of numbers.
    2. Your task is to create a multiplication matrix that only includes multiples of a given number.
    E.G
    INPUT:  numbers = [1, 2, 3, 4, 5, 6]
            multiple_of = 2

    OUTPUT: [4, 8, 12]
            [8, 16, 24]
            [12, 24, 36]
'''

'''
     1. What I know is that mulples of a given number should be divisable evenly with no remainder
'''


def multiples_matrix(numbers: list, multiple_of: int) -> list:
    filtered =[]
    all_the_matrixes = []
    multiplied = []
    # In this first loop I was just accessing those number that divisable till 0
    for i in numbers:
        if i % multiple_of ==  0:
            filtered.append(i)
    for i in filtered:
        for j in filtered:
            multiplied.append(i*j)
        all_the_matrixes.append(multiplied)
        multiplied = []
    for i in all_the_matrixes:
        print(i)
    return all_the_matrixes



numbers = [1, 2, 3, 4, 5, 6]
multiple_of = 2
multiples_matrix(numbers, multiple_of)
