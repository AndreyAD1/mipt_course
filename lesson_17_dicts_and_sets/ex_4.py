from collections import Counter
import copy
import string


def get_word_frequency(text: str):
    """Функция возвращает количество повторений каждого слова текста

    :param text:
    :return:
    """
    processed_text = copy.deepcopy(text)

    for symbol in string.punctuation:
        processed_text = processed_text.replace(symbol, ' ')

    word_list = processed_text.lower().split()
    word_counter = Counter(word_list)
    return word_counter.most_common()


if __name__ == '__main__':
    with open('../lesson2/robot-tasks-master/pyrob/LICENSE', 'r') as file:
        text = file.read()

    most_frequent_word, word_number = get_word_frequency(text)[0]
    print(
        'Самое часто повторяющееся слово: {}. Количество повторений: {}'.format(
            most_frequent_word,
            word_number
        )
    )
