

# CHALLANGE 6: MIXED DATA PATTERN MATRIX

'''
    Challange 6: MIXED DATA PATTERN MATRIX
    Description: 
    You are given a list that contains both numbers and words.
        1. Filter the list so that numbers satisfy a certain divisibility rule, and words satisfy a length rule.
        2. Using nested loops, generate a matrix where:
        3. Numbers are combined with numbers through multiplication
        4. Words are concatenated with words
        5. Numbers and words can also interact in some way
        6. Skip combinations that meet a certain “skip condition” based on length or value.
        7. The output should clearly differentiate rows generated from numbers vs. rows generated from words, but still keep everything in one matrix.
Your goal is to produce the matrix using only nested loops and conditionals — no fancy shortcuts, no sets, no built-in filter functions.
    EXAMPLE: 
        INPUT:
            mixed_list = [2, "hi", 4, "tree", 5, "sun", 6, "moon"]
            number_divisible_by = 2
            word_length_divisible_by = 2
            skip_value_or_length = 8
        
        OUTPUT:
            [4, 12]           # numbers multiplied, skipping multiples of 8
            ['hihi', 'hitree', 'himoon']               # words concatenated, skipping length divisible by 8
            ['treehi']
            [12, 36]               # next number row
            ['moonhi'] # next word row

'''

'''
    My understanding: first filter nums and words:  so nums=[2,4,6]  and words=["hi","tree","moon"] combined= [2,4,6,"hi","tree","moon"]
    now I have to check digit and alpha:
        then for numbers will be 2*2=4 2*4=8 2*6=12 so first will be [4,12]
        then for alphas will be "hihi" "hitree" "himoon" so first will be all of this 3 
'''


def mixed_data_matrix(mixed_list: list, number_div_by: int, word_len_div_by: int, skip_value_or_length: int) -> list:
    filtered = []
    matrix = []
    nums_filtered = []
    words_filtered = []
    for i in mixed_list:
        if isinstance(i, int) and i % number_div_by == 0:
            filtered.append(i)
        elif isinstance(i, str) and len(i) % word_len_div_by == 0:
            filtered.append(i)
    # print(filtered)

    for i in filtered:
        for j in filtered:
            if isinstance(i, int) and isinstance(j, int):
                if not (i*j) % skip_value_or_length == 0:
                    nums_filtered.append(i*j)

            elif isinstance(i, str) and isinstance(j, str):
                if not len(i+j) % skip_value_or_length == 0:
                    words_filtered.append(i+j)
        if len(nums_filtered) > 0:
            matrix.append(nums_filtered)
            nums_filtered = []
        if len(words_filtered) > 0:
            matrix.append(words_filtered)
            words_filtered = []
    for i in matrix:
        print(i)

    return (matrix)


mixed_list = [2, "hi", 4, "tree", 5, "sun", 6, "moon"]
number_divisible_by = 2
word_length_divisible_by = 2
skip_value_or_length = 8

mixed_data_matrix(mixed_list, number_divisible_by, word_length_divisible_by, skip_value_or_length)