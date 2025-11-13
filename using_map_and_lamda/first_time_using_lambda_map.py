
# Using lamda and map

# first 1
def first():
    numbers = [1, 2, 3, 4, 5] # should return [1, 4, 9, 16, 25]
    x = list(map(lambda x: x*x,numbers))
    print(x)

# Second 
# Task: Convert all to Fahrenheit using formula (°C * 9/5) + 32
def second():
    temps_c = [0, 10, 20, 30, 40]
    y = list(map(lambda x: ((x*9/5)+35),temps_c) )
    print(y)

# third
# Task: Use map + lambda to make each name start with a capital letter
def third():
    names = ['njabulo', 'thabo', 'amanda']
    cap = list(map(lambda x: x.capitalize(), names))
    print(cap)


# Level 2: Medium

# Task4: Return a list of the lengths of each word
def fourth():
    words = ['python', 'lambda', 'map', 'function']
    length = list(map(lambda x: len(x), words))
    print(length)


# Task5: Return a new list like ['odd', 'odd', 'even', 'even', 'odd', 'even']
def fifth():
    nums = [3, 7, 8, 10, 15, 22]
    even_odd = list(map(lambda x: "even" if x%2==0 else "odd", nums))
    print(even_odd)


# Task6: Use map + lambda to return final prices after discounts
def sixth():
    prices = [100, 200, 300]
    discounts = [10, 20, 15]  # percentages
    total = list(map(lambda x: x[0] - (x[0] * (x[1]/100)), zip(prices, discounts)))
    print(total)


# 💡 Level 3: Advanced

# Task: Use map + lambda to get [1, 4, 9, 16, 25, 36]
def seventh():
    nested = [[1, 2], [3, 4], [5, 6]]
    flatten = list(map(lambda x: x*x if isinstance(x, int) else [i*i for i in x],nested))
    clear = []
    for i in flatten:
        if isinstance(i, list):
            clear.extend(i)
    print(clear)


# Task8: Return ['EM', 'MZ', 'BG'] using map + lambda
def eighth():
    names = ["Elon Musk", "Mark Zuckerberg", "Bill Gates"]
    initials = list(map(lambda x: ''.join([i[0] for i in x.split()]) , names))
    print(initials)


# Task9: Create a map + lambda that doubles even numbers and halves odd numbers
# (even though here all are even — try testing both cases)
def nineth():
    nums = [2, 4, 6, 8, 9, 11]
    double_halve = list(map(lambda x: x*2 if x%2==0 else x/2, nums))
    print(double_halve)

# Task: Use a map and a nested lambda to return [1, 8, 27] (cube each number)
nums = [1, 2, 3]
cube = list(map(lambda x:, y=x lambda :y lambda z: (x*y*z) ,nums))