def merge_the_tools(string: str, k: int) -> None:
    """
    Делит строку string на k подстрок.
    Этот вариант - в каждой подстроке удаляет ВСЕ дубликаты символов.
    AAABA -> AB

    CACAC -> CA

    :param string: 'AAABACACAC'
    :param k: 5
    :return:
    """

    for i in range(0, len(string), k):
        substring = string[i:i + k]
        sample = list()
        [sample.append(char) for char in substring if char not in sample]

        print(''.join(sample))


def merge_the_tools2(string: str, k: int) -> None:
    """
    Делит строку string на k подстрок.
    Этот вариант - в каждой подстроке удаляет все ПОДРЯД ИДУЩИЕ дубликаты символов.
    AAABA -> ABA

    CACAC -> CACAC

    :param string: 'AAABACACAC'
    :param k: 5
    :return: None
    """

    substrings = list()
    [substrings.append(string[i:i+k]) for i in range(0, len(string), k)]

    for s in substrings:
        sample = str()
        previous = str()

        for char in s:
            if char != previous:
                previous = char
                sample += char

        print(sample)


if __name__ == '__main__':
    # merge_the_tools('AABCAAADA', 3)
    # merge_the_tools('AAABCADDEABB', 3)
    # merge_the_tools('AAABCADDEABB', 4)
    merge_the_tools('AAABACACAC', 5)
    merge_the_tools2('AAABACACAC', 5)
