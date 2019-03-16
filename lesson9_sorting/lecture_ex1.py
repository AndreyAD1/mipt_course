# Сортировка слиянием


def merge_sort(a: list):
    if len(a) <= 1:
        return
    middle = len(a) // 2
    left_half = [a[i] for i in range(0, middle)]
    right_half = [a[i] for i in range(middle, len(a))]
    merge_sort(left_half)
    merge_sort(right_half)
    c = merge(left_half, right_half)
    for i in range(len(a)):
        a[i] = c[i]
    return a


def merge(a: list, b: list):
    c = [0] * (len(a) + len(b))
    i = k = n = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]: # = для устойчивости сортировки
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1
    while i < len(a):
        c[n] = a[i]
        i += 1
        n += 1
    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1
    return c


s = [3, 7, 99, -5, 0, 5.6]
print(merge_sort(s))
