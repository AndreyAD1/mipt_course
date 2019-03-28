from ex_2_check_brackets import check_brackets


def to_reverse_polish_notation(infix_notation: str):
    output = []
    operator_stack = []
    operators = {'+': (1, True), '-': (1, False), '*': (2, True), '/': (2, False)}

    if not check_brackets(infix_notation):
        return
    input = infix_notation.split(' ')

    for element in input:
        if element in operators:
            if not operator_stack:
                operator_stack.append(element)
            else:
                operator_in_stack = operator_stack[-1]
                if operator_in_stack == '(':
                    operator_stack.append(element)
                    continue
                priority_in_stack, associativity = operators[operator_in_stack]
                current_priority, _ = operators[element]

                while operator_in_stack != '(' and (
                        (
                            current_priority == priority_in_stack and not associativity
                        ) or current_priority < priority_in_stack
                ):
                    output.append(operator_stack.pop())
                    if not operator_stack:
                        break
                    operator_in_stack = operator_stack[-1]
                    priority_in_stack, associativity = operators[operator_in_stack]

                operator_stack.append(element)
        elif element == '(':
            operator_stack.append(element)
        elif element == ')':
            operator = operator_stack.pop()
            while operator != '(':
                output.append(operator)
                operator = operator_stack.pop()
        else:
            output.append(element)

    while operator_stack:
        output.append(operator_stack.pop())

    return output


if __name__ == '__main__':
    expression = '1 + 3 * 5 - 10'
    converted_expression = to_reverse_polish_notation(expression)
    if not converted_expression:
        exit('Invalid brackets')
    print(converted_expression)

    expression = '( 1 + 3 ) * 5 - 10'
    converted_expression = to_reverse_polish_notation(expression)
    if not converted_expression:
        exit('Invalid brackets')
    print(converted_expression)

    expression = '( 1 + 3 ) * ( 5 - 10 )'
    converted_expression = to_reverse_polish_notation(expression)
    if not converted_expression:
        exit('Invalid brackets')
    print(converted_expression)

    expression = '( 1 + 3 * 10 ) / ( 5 - 10 ) * 4'
    converted_expression = to_reverse_polish_notation(expression)
    if not converted_expression:
        exit('Invalid brackets')
    print(converted_expression)

    expression = '( 1 + 3 * 10 ) / ( 5 - 10 ) * 4 + 1 / ( 2 + 1 )'
    converted_expression = to_reverse_polish_notation(expression)
    if not converted_expression:
        exit('Invalid brackets')
    print(converted_expression)
