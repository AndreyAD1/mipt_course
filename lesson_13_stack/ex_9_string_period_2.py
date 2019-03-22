from prefix_function import get_prefixes


def get_min_string_period(string: str) -> str:
    prefix_function = get_prefixes(string)
    last_suffix_length = prefix_function[-1]
    string_length = len(string)
    period = None
    for index, suffix_length in enumerate(prefix_function):
        if last_suffix_length == string_length - index and last_suffix_length > index - 1:
            period = string[:index]
            break
        elif index > string_length // 2:
            break
        else:
            continue

    return period


if __name__ == '__main__':
    string = 'aaaaa'
    print(get_min_string_period(string))
    string = 'abacaabaca'
    print(get_min_string_period(string))
    string = 'abcdefg_abcdefg1_abcdefg_abcdefg1_abcdefg_abcdefg1_abcdefg_abcdefg1_'
    print(get_min_string_period(string))
    string = 'abacaba'
    print(get_min_string_period(string))
    string = 'abaabafdcabaaba'
    print(get_min_string_period(string))
    string = 'abcdefg'
    print(get_min_string_period(string))
    string = 'abcdefgi'
    print(get_min_string_period(string))
    string = 'abcdefgi_abcdefgi'
    print(get_min_string_period(string))

    string = 'abcdefgi_abcdefgi_'
    print(get_min_string_period(string))

