def check_brackets(math_expression: str) -> bool:
    bracket_types = {')': '(', ']': '['}
    bracket_stack = []
    for symbol in math_expression:
        if symbol in bracket_types.values():
            bracket_stack.append(symbol)
        if symbol in bracket_types.keys():
            if not bracket_stack:
                return False
            else:
                previous_open_bracket = bracket_stack.pop()
                expected_open_bracket = bracket_types[symbol]
                if previous_open_bracket != expected_open_bracket:
                    return False
    if not bracket_stack:
        return True
    return False


if __name__ == '__main__':
    expression = 'a + (b - [c * 2])'
    print(check_brackets(expression))
