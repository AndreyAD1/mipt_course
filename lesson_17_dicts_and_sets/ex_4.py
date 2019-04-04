from collections import Counter


def get_word_frequency(text: str):
    """Функция возвращает количество повторений каждого слова текста

    :param text:
    :return:
    """
    # Заменить пунктуацию на пробелы
    # разделить текст на слова
    # создать объект Counter
    # вернуть Counter.items()
    pass


if __name__ == '__main__':
    with open('../lesson2/robot-tasks-master/pyrob/LICENSE', 'r') as file:
        text = file.read()

    print(text)
