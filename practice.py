from collections import Counter

dict_one = {'a': 1, 'b': 2, 'c': 3}
dict_two = {'d': 1, 'e': 2, 'f': 3, 'a': 99}

def add_dicts(dict_one, dict_two):
    return dict(Counter(dict_one) + Counter(dict_two))