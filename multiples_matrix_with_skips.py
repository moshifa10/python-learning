

# Challange 4

'''
    Challange 4: Multiplication Matrix with Skips
    Description: You’re given:
        1. A list of numbers
        2. A number to filter multiples (multiple_of)
        3. A number to skip multiples of (skip_multiple_of)

    EXAMPLE:
        INPUT:
            numbers = [1, 2, 3, 4, 5, 6]
            multiple_of = 2
            skip_multiple_of = 8
        OUTPUT: 
            [4, 12]
            []
            [12, 36]
'''

'''
    Okay : first get this [2,4,6]
        second multiply 2 * 2 = 4, 2 * 4 = 8, 2*6= 12 this should [4,12] -> only 
'''


def multiples_matrix_with_skips(numbers: list, multiple_of: int, skip_multiple_of: int) -> list:
    # First find the multiple_of to loop through it

    
    multiple_nums = []
    matrix = [] 
    multiplied = []
    for i in numbers:
        if i % multiple_of == 0:
            multiple_nums.append(i)
    
    # So now I found multiples I should focus on multiple each and every item in multiple_nums and filter

    for i in multiple_nums:
        for j in multiple_nums:
            if not (i*j) % skip_multiple_of == 0:
                multiplied.append(i*j)
        if len(multiplied) > 0:
            matrix.append(multiplied)
            multiplied = []

    for i in matrix:
        print(i)

    return matrix

numbers = [1, 2, 3, 4, 5, 6]
multiple_of = 2
skip_multiple_of = 8
multiples_matrix_with_skips(numbers, multiple_of, skip_multiple_of)

    

