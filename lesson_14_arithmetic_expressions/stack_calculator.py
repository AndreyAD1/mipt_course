def calculate(expression: list) -> (float, None):
    stack = []
    digit_counter = 0
    for token in expression:
        # write a RE matching all kind of numbers
        if type(token) in (int, float):
            stack.append(float(token))
            digit_counter += 1
        else:
            if digit_counter > 2 or len(stack) < 2:
                return 'Invalid expression near {}'.format(token)
            digit_counter = 0
            operand_2 = stack.pop()
            operand_1 = stack.pop()

            if token == '+':
                result = operand_1 + operand_2
            elif token == '-':
                result = operand_1 - operand_2
            elif token == '*':
                result = operand_1 * operand_2
            elif token == '/':
                result = operand_1 / operand_2
            else:
                return 'Unknown operator: {}'.format(token)

            stack.append(result)
    return stack.pop()


if __name__ == '__main__':
    expression = [2, 3, '+']
    print(calculate(expression))

    expression = [2, 3, '+', 5, '*']
    print(calculate(expression))

    expression = [2, 3, '-', 12, 10, '-', '*', 4, 2, '/']
    print(calculate(expression))

    expression = ['+', 2, 3]
    print(calculate(expression))

    expression = [2, 3, 4, '+']
    print(calculate(expression))

    expression = [2, 3, '+', 5, '*', '/']
    print(calculate(expression))

    expression = [2, 3, '+', 5, '?']
    print(calculate(expression))
