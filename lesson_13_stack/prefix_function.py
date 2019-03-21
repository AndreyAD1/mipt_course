def get_prefixes(string):
    prefixes = [0] * len(string)
    for symbol_index in range(1, len(string)):
        prefix_length = prefixes[symbol_index - 1]

        while prefix_length > 0 and string[symbol_index] != string[prefix_length]:
            prefix_length = prefixes[prefix_length - 1]

        if string[symbol_index] == string[prefix_length]:
            prefix_length += 1

        prefixes[symbol_index] = prefix_length
    return prefixes


def substring_search(substring, string):
    search_string = substring + '#' + string
    prefixes = get_prefixes(search_string)
    if len(substring) in prefixes:
        return True
    return False


def kmp_algorithm(substring, string):
    search_string = substring + '#' + string
    prefixes = get_prefixes(search_string)
    substring_start_indexes = []
    for symbol_index, prefix_length in enumerate(prefixes[(len(substring) + 1):]):
        if prefix_length == len(substring):
            substring_start_indexes.append(symbol_index - prefix_length + 1)
    return substring_start_indexes


if __name__ == '__main__':
    string = 'abcadabcaasdawabcdas'
    # print(substring_search('aw1d', string))
    print(kmp_algorithm('abc', string))

    string = 'abcabcd'
    print(get_prefixes(string))

    string = 'aabaaab'
    print(get_prefixes(string))

    string = 'abc#abcadabcaasdawdas'
    print(get_prefixes(string))

