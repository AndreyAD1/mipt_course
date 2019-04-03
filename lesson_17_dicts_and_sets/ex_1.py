import matplotlib.pyplot as plt
import time


def get_pop_time(size, repeat_count, pop_position=None):
    """
    size - размер списка из нулей на котором будем тестировать скорость операции pop
    repeat_count - количество повторений для усреднения
    pop_position - позиция с которой делаем pop
    """
    list_of_lists = []
    for _ in range(repeat_count):
        list_of_lists.append([0] * size)
    pop_position = -1 if pop_position is None else pop_position
    start_time = time.time()

    for list in list_of_lists:
        list.pop(pop_position)

    end_time = time.time()
    return (end_time - start_time) / repeat_count


repeat_count = 1000
pop_position = 10
# code here
values1 = [get_pop_time(size, repeat_count) for size in range(10, 1000)]
values2 = [get_pop_time(size, repeat_count, 0) for size in range(10, 1000)]
values3 = [get_pop_time(size, repeat_count, -1) for size in range(10, 1000)]

plt.plot(values1, label='Pop no args')
plt.plot(values2, label='Pop start list')
plt.plot(values3, label='Pop end list')
plt.ylabel('pop time')
ax = plt.subplot(111)
plt.legend()
# ax.legend()
plt.show()
