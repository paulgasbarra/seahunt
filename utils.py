def get_dict_difference(dict1, dict2):
    set1 = set(dict1)
    set2 = set(dict2)
    return set1 ^ set2