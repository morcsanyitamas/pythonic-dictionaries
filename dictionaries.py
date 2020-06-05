def merge_dicts(dict_one, dict_two):
    # Flake8 won't cry because of the first one. For second one it will.
    # {dict_two.update({key: value}) if key not in dict_two.keys() else dict_two.update({key: (dict_two[key] + dict_one[key])}) for key, value in dict_one.items()}
    # for key, value in dict_one.items(): dict_two.update({key: value}) if key not in dict_two.keys() else dict_two.update({key: (dict_two[key] + dict_one[key])})
    {dict_two.update({key: value}) if key not in dict_two.keys() else dict_two.update(
        {key: (dict_two[key] + dict_one[key])}) for key, value in dict_one.items()}
    return dict_two


dict_one = {'a': 1, 'b': 2, 'c': 3}
dict_two = {'d': 1, 'e': 2, 'f': 3, 'a': 99, }
print(merge_dicts(dict_one, dict_two))
