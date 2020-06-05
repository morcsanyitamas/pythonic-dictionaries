def concat(dict_one, dict_two):
    [dict_one.update({key: (dict_one[key]+dict_two[key])}) if key in dict_one else dict_one.update({key: dict_two[key]}) for key in dict_two]
    return dict_one


print(concat(dict_one, dict_two))