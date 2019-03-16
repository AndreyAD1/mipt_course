def trivial_algorithm(prefix_length, string, index):
    while index + prefix_length < len(string) and string[prefix_length] == string[index + prefix_length]:
        prefix_length += 1
    return prefix_length


def get_z_function(string: str) -> list:
    z_array = []
    for index, symbol in enumerate(string):
        z_array.append(0)
        if index == 0:
            continue
        while index + z_array[index] < len(string) and string[z_array[index]] == string[index + z_array[index]]:
            z_array[index] += 1
    return z_array


def get_z_function_effectively(string: str) -> list:
    z_array = []
    rightmost_found_prefix_index = 0
    leftmost_found_prefix_index = 0
    for index, symbol in enumerate(string):
        if index == 0:
            z_array.append(0)
            continue
        if index > rightmost_found_prefix_index:
            prefix_length = 0
        else:
            prefix_length = min(
                z_array[index - leftmost_found_prefix_index],
                rightmost_found_prefix_index - index + 1
            )
        while index + prefix_length < len(string) and string[prefix_length] == string[index + prefix_length]:
            prefix_length += 1
        z_array.append(prefix_length)
        prefix_end_index = index + prefix_length - 1
        if prefix_end_index > rightmost_found_prefix_index:
            leftmost_found_prefix_index = index
            rightmost_found_prefix_index = prefix_end_index
    return z_array


if __name__ == '__main__':
    string = 'aaaaa'
    print(get_z_function(string))
    string = 'abaaba'
    print(get_z_function(string))
    string = 'aaabaab'
    print(get_z_function(string))
    string = 'abacaba'
    print(get_z_function(string))

    print()

    string = 'aaaaa'
    print(get_z_function_effectively(string))
    string = 'abaaba'
    print(get_z_function_effectively(string))
    string = 'abaabaaba'
    print(get_z_function_effectively(string))
    string = 'aabaab'
    print(get_z_function_effectively(string))
    string = 'abacabacabacabac'
    print(get_z_function_effectively(string))
    string = 'abcdefg_abcdefg1_abcdefg_abcdefg1_abcdefg_abcdefg1_abcdefg_abcdefg1_'
    print(get_z_function_effectively(string))
    string = 'abacaba'
    print(get_z_function_effectively(string))
