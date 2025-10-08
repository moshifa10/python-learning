

# Challange 5

'''
    CHALLANGE 5: Word Pattern Matrix

    DESCRIPTION: 
        1. Include only words with length divisible by length_of.
        2. For each word in the filtered list, create a row by concatenating it with every word in the filtered list.
        3. Skip concatenations where the combined length is divisible by skip_length.
        4. Print each row.

    EXAMPLE:
        INPUT:
            words = ["hi", "cat", "dog", "tree", "sun"]
            length_of = 2
            skip_length = 6
        OUTPUT:
            ["hihi"]
            ["treetree"]
'''

'''
    My pattern: "hi", "tree"  -> will be on Filtered since the length is divisable by 2
    Okay then:
        first loop "hihi" -> len of 4 and not divisable by 6 so correct,
        then "hitree" -> len of 6 and this is divisable by 6 so just continue
        second treehi same as hitree same length just continue
        then "treetree" len of 8 and this is not divisable by and give me 0 as it has a remainder
'''

def find_word_pattern(words: list, length_of: int, skip_length: int) -> list:
    filtered = []
    conca = ""
    matrix = []

    for i in words:
        if len(i) % length_of == 0:
            filtered.append(i)

    for i in filtered:
        for j in filtered:
            if not len(i+j) % skip_length == 0:
                conca += i+j
        matrix.append(conca)
        conca = ""

    for i in matrix:
        print(i)
    return matrix

words = ["hi", "cat", "dog", "tree", "sun"]
length_of = 2
skip_length = 6
find_word_pattern(words, length_of, skip_length)
