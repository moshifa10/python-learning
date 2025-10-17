
# Challange 20


def find_anagram_groups(words: list[str]) -> list[list[str]]:
    """
    Group words that are anagrams of each other.
    
    Example:
        Input → words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        Output → [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    """
    my_dict ={}
    for i in words:
        key = "".join(sorted(i))
        if len(my_dict) == 0:
            my_dict[key] = f"{i} "
        elif key not in  my_dict:
            my_dict[key] = f"{i} "
        else:
            my_dict[key] += f"{i} "
    correct_list = []
    for i in my_dict:
        if my_dict[i].split() not in correct_list:
            correct_list.append(my_dict[i].split())

    print(correct_list)
    # relation = []
    # for i in range(len(words)):
    #     relation.append([p for p in words if sorted(words[i]) == sorted(p)])

    # print(relation)
    # correct_list = []
    # for i in range(len(relation)):
    #     if not relation[i] in correct_list:
    #         correct_list.append(relation[i])
    # return correct_list
    # relation = {}
    # for count,i in enumerate(words):
    #     if sorted(i) not in relation:
    #         relation[sorted(i)] = [count]
    #     else: 
    #         relation[sorted(i)]  count 

    # print(relation)


find_anagram_groups(["eat", "tea", "tan", "ate", "nat", "bat"])
