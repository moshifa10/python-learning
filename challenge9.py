import string

# CHALLANGE 9 

'''
    Challange 9: Text frequency analyzer
    Goal: Create a program that analyzes a given block of text and tells you how often each word appears
            like a mini AI that counts and ranks words in a paragraph

    Example:
        Input:
            text = "Hello world! Hello Njabulo, you are doing great. Keep going, Njabulo!"

        Output:
            {
            "word_count": {
                "hello": 2,
                "world": 1,
                "njabulo": 2,
                "you": 1,
                "are": 1,
                "doing": 1,
                "great": 1,
                "keep": 1,
                "going": 1
            },
            "most_common": "hello",
            "unique_words": [
                "are", "doing", "going", "great", "hello", "keep", "njabulo", "world", "you"
            ]
            }            

'''

def text_analyzer(text: str, top_n=3) -> dict:
    analyzer = {}
    word_count ={}
    
    for i in text:
        if i in string.punctuation:
            text = text.replace(i, "")
    text = text.lower().split()
    
    for i in range(len(text)):
        count = text.count(text[i])
        word_count[text[i]]= count

    count = 0
    name = ""
    for i in word_count:
        if word_count[i] > count:
            count = word_count[i]
            name = i

    unique_words = []
    for unique in word_count:
        if word_count[unique] == 1:
            unique_words.append(unique)

    analyzer["word_count"] = word_count
    analyzer["most_common"] = name
    analyzer["unique_words"] = unique_words
    
    

    print(analyzer)

text = "Hello world! Hello Njabulo, you are doing great. Keep going, Njabulo!"
text_analyzer(text)
# print(string.punctuation)