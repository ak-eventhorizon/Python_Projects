def snail(arr_2d: list) -> list:
    """
    Улиточная сортировка двумерной матрицы.

    :param arr_2d:  [[1, 2, 3],
                     [8, 9, 4],
                     [7, 6, 5]]
    :return: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """

    result = list()

    y_start = 0
    y_end = len(arr_2d) - 1
    x_start = 0
    x_end = len(arr_2d[0]) - 1

    while y_start <= y_end and x_start <= x_end:
        for i in range(x_start, x_end + 1):
            result.append(arr_2d[y_start][i])
        y_start += 1

        for i in range(y_start, y_end + 1):
            result.append(arr_2d[i][x_end])
        x_end -= 1

        if y_start <= y_end:
            for i in range(x_end, x_start - 1, -1):
                result.append(arr_2d[y_end][i])
        y_end -= 1

        if x_start <= x_end:
            for i in range(y_end, y_start - 1, -1):
                result.append(arr_2d[i][x_start])
        x_start += 1

    return result


if __name__ == '__main__':
    arr1 = [[1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]]

    arr2 = [[1, 1, 1, 1],
            [2, 3, 3, 1],
            [2, 4, 3, 1],
            [2, 2, 2, 1]]

    arr3 = [['H', 'e', 'l', 'l', 'o'],
            ['l', 'S', 'o', 'r', 'T'],
            ['i', 'l', '!', 't', 'h'],
            ['a', 'i', 't', 'U', 'i'],
            ['n', 'S', 's', 'I', 's']]

    # print(snail(arr1))  # -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(snail(arr2))  # -> [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4]
    print(''.join(snail(arr3)))  # -> HelloThisIsSnailSortUtil!
