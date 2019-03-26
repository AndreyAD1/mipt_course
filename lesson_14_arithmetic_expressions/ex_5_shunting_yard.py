from ex_2_check_brackets import check_brackets


def to_reverse_polish_notation(infix_notation: str):
    output = []
    operator_stack = []
    known_operators = '+-*/'

    if not check_brackets(infix_notation):
        return
    input = infix_notation.split(' ')

    for element in input:
        if element in known_operators:
            pass
        elif element == '(':
            operator_stack.append(element)
        elif element == ')':
            pass
        else:
            output.append(element)

    return input


if __name__ == '__main__':
    expression = '1 + 3 * 5 - 10'
    converted_expression = to_reverse_polish_notation(expression)
    if not converted_expression:
        print('Invalid brackets')
