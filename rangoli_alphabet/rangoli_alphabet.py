def rangoli_transform(num: int) -> str:
    """Рисование паттерна Rangoli.

    num = 3 ->

    ----c----\n
    --c-b-c--\n
    c-b-a-b-c\n
    --c-b-c--\n
    ----c----\n

    :param num: число, определяющее размер паттерна Rangoli
    :return:  строка с готовым паттерном
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = list()

    if not 0 < num < 27:
        print('Input value is out of range (0 < N < 27)')
        return ''

    # отрезаем от алфавита нужную часть для построения фигуры
    max_slice = alphabet[:num]  # abcde

    # создаем центральную строку узора
    center_string = max_slice[::-1] + max_slice[1:]  # edcba + bcde
    center_string = '-'.join(list(center_string))  # e-d-c-b-a-b-c-d-e

    # ширина всего узора равна ширине центральной строки
    pattern_width = len(center_string)

    for i in range(num):
        current_slice = alphabet[i:num]

        pattern = current_slice[::-1] + current_slice[1:]
        pattern = "-".join(list(pattern))

        result.append(pattern.center(pattern_width, '-'))

    result = result[::-1] + result[1:]

    return '\n'.join(result)


if __name__ == '__main__':
    print(rangoli_transform(5))
