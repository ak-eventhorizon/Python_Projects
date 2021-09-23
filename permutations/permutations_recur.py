result = list()


def permutations(string: str, index=0):
    """Recursion implementation of string permutations"""

    # когда добрались до последней позиции - возвращаем пермутацию
    if index == len(string):
        result.append(''.join(string))

    # все что правее позиции - еще не перемешивалось в комбинации
    for i in range(index, len(string)):

        # строку в список посимвольно
        listed_string = [char for char in string]

        # меняем элементы местами
        listed_string[index], listed_string[i] = listed_string[i], listed_string[index]

        # рекурсивно перемешиваем элементы
        permutations(listed_string, index + 1)


if __name__ == '__main__':
    permutations('aabb')
    print(result)
    print(set(result))
