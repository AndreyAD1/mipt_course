def hoar_sort(a: list):
    if len(a) <= 1:
        return
    barrier = a[0]
    left_part = []
    middle_part = []
    right_part = []
    for x in a:
        if x < barrier:
            left_part.append(x)
        elif x == barrier:
            middle_part.append(x)
        else:
            right_part.append(x)
    hoar_sort(left_part)
    hoar_sort(right_part)
    k = 0
    for x in left_part + middle_part + right_part:
        a[k] = x
        k += 1


s = [1, -4, -100, 0, 99, 3, 7, 4, 5, 5, -4]
hoar_sort(s)
print(s)
