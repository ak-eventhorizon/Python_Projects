import itertools


def maximize_it(iterations: int, mod: int) -> None:
    """
    :param iterations: сколько списков ожидается от пользователя
    :param mod: модуль деления для получения остатка ( % mod)
    :return:
    """

    list_of_lists = list()
    for i in range(iterations):
        list_of_lists.append(list(map(int, input().split()))[1:])  # первый элемент игнорируется по условию задачи

    all_combinations = list(itertools.product(*list_of_lists))  # все комбинации элементов всех списков
    list_of_results = list()

    for comb in all_combinations:
        list_of_results.append(sum([i**2 for i in comb]) % mod)

    # print(list_of_lists)
    # print(all_combinations)
    # print(list_of_results)
    print(max(list_of_results))


if __name__ == '__main__':
    n, m = list(map(int, input().split()))  # n - количество ожидаемых списков, m - модуль деления для получения остатка
    maximize_it(n, m)
