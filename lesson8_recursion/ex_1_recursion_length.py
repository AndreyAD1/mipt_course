def factorial(n, recursion_step=0):
    try:
        if n == 0:
            return 1
        else:
            recursion_step += 1
            return n * factorial(n-1, recursion_step)
    except RecursionError:
        exit('Recursion limit is {}'.format(recursion_step))


print(factorial(-5))
