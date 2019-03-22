def check_brackets(math_expression: str) -> bool:
    brackets = '()[]'
    bracket_stack = []
    for symbol in math_expression:
        if symbol in '([':
            bracket_stack.append(symbol)
        if symbol in ')]':
            if not bracket_stack:
                return False
            else:
                previous_open_bracket = bracket_stack.pop()
                if previous_open_bracket != symbol:
                    return False
    if not bracket_stack:
        return True
    return False


if __name__ == '__main__':
    expression = 'a + (b - c)'
    print(check_brackets(expression))
