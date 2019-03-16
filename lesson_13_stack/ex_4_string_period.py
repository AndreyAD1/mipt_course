from ex_1_z_function import get_z_function_effectively


def get_min_string_period(string: str) -> str:
    z_function = get_z_function_effectively(string)
    reversed_z_function = z_function[::-1]
    period_index = 0
    for index, prefix_length in enumerate(reversed_z_function):
        initial_index = index
        initial_prefix_length = prefix_length
        while prefix_length == index + 1 and index < len(reversed_z_function):
            index = initial_prefix_length + index
            prefix_length = reversed_z_function[index]
        if index == len(reversed_z_function) - 1:
            period_index = len(string) - initial_index - 1
            break
    return string[period_index:]


if __name__ == '__main__':
    string = 'aaaaa'
    print(get_min_string_period(string))
    string = 'abacabacabacabac'
    print(get_min_string_period(string))
    string = 'abcdefg_abcdefg1_abcdefg_abcdefg1_abcdefg_abcdefg1_abcdefg_abcdefg1_'
    print(get_min_string_period(string))
    string = 'abacaba'
    print(get_min_string_period(string))
