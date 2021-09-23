from itertools import permutations


def show_permutations(string: str) -> None:
    """Пишет в файл все варианты пермутаций указанной строки"""

    result = list(permutations(string))

    with open('output.txt', 'w') as file:
        for elem in result:
            file.write(''.join(elem) + '\n')


if __name__ == '__main__':
    show_permutations(input('String for permutation: '))
