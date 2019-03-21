from ex_1_z_function import get_z_function_effectively


def get_min_string_period(string: str) -> str:
    z_function = get_z_function_effectively(string)
    last_index = len(string)
    for index, prefix_length in enumerate(z_function):
        if index + prefix_length == last_index and not last_index % index:
            return string[:index]


if __name__ == '__main__':
    string = 'aaaaa'
    print(get_min_string_period(string))
    string = 'abacabacabacabac'
    print(get_min_string_period(string))
    string = 'abcdefg_abcdefg1_abcdefg_abcdefg1_abcdefg_abcdefg1_abcdefg_abcdefg1_'
    print(get_min_string_period(string))
    string = 'abacaba'
    print(get_min_string_period(string))
