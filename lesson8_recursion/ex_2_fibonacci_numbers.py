def fibonacci_counter(number_index):
    lower_number = 0
    upper_number = 1
    for i in range(number_index-1):
        next_number = lower_number + upper_number
        lower_number = upper_number
        upper_number = next_number
    return next_number


print(fibonacci_counter(8))


def fib_recursive_counter(index):
    assert index >= 0
    if index == 0:
        return 0
    if index == 1:
        return 1
    if index > 1:
        return fib_recursive_counter(index-1) + fib_recursive_counter(index - 2)


print(fib_recursive_counter(10))
