from prefix_function import kmp_algorithm


def online_substring_search(input_string):
    lines = input_string.splitlines()
    pattern = lines[0]
    text_list = lines[1:]
    text = ''.join(text_list)
    return kmp_algorithm(pattern, text)


if __name__ == '__main__':
    string = '''abc
a
b
c
d
e
f
a
b
c
l
k
abc
'''
    print(online_substring_search(string))
