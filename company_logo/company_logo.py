from collections import defaultdict

def main(s: str) -> None:
    """
    Выводит три наиболее часто встречающихся символа в переданной строке.
    Если количество вхождений у символов одинаковое - предпочтение отдается
    по алфавитному порядку

    :param s:
    :return:
    """

    # получаем словарь, где key - символ строки, value - число его вхождений в строке
    d = defaultdict(int)
    for i in s:
        d[i] += 1

    # сортируем по ключу (символы) элементы с одинаковых значением (количеством вхождений)
    sorted_d = [v for v in sorted(d.items(), key=lambda i: (-i[1], i[0]))]

    # выводим первые три пары
    for i in range(3):
        print(f'{sorted_d[i][0]} {sorted_d[i][1]}')


if __name__ == '__main__':
    # main('google')  # g 2   o 2   e 1
    main('aabbbccde')  # b 3   a 2   c 2
    # main('eccdaabbb')  # b 3   a 2   c 2
