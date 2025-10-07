

# Second challange 
# I am happy 
# I will keep the streak going


'''
        Challange 2: Challenge #2: “Find Common Elements Between Two Lists”
            1. You’re given two lists of numbers.
            2. You must find and print all the numbers that appear in both lists (the intersection).


Key : You must do it using nested loops only — 
            no sets, no list comprehensions, and no built-in intersection functions.
'''

def common_elements(list1: list, list2: list) -> list:
    common = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j] and list1[i] not in common:
                common.append(list1[i])


    print(f"Common elements: {common}")
    return common

# list1 = [2, 4, 6, 8, 10]
# list2 = [3, 4, 6, 9, 10]
list1 = ["apple", "banana", "pear"]
list2 = ["banana", "cherry", "apple"]
common_elements(list1, list2)




