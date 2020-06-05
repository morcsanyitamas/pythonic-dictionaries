
def merge(dict_one, dict_two):
    return {**dict_two, **{key: (dict_one.get(key) + dict_two.get(key, 0)) for key in dict_one}}


def main():
    dict_one = {'a': 1, 'b': 2, 'c': 3}
    dict_two = {'d': 1, 'e': 2, 'f': 3, 'a': 99}

    dict_final = merge(dict_one, dict_two)
    print(dict_final)


if __name__ == "__main__":
    main()
