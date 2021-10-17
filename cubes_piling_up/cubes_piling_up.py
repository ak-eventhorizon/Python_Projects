def piling_up(arr: list) -> None:
    """
    На вход передается список, обозначающий ряд кубиков (размер стороны каждого кубика)
    Задача - вывести ответ (Yes/No) - возможно ли построить из этих кубиков башню, если каждую
    итерацию брать один кубик - крайний слева или справа. Размер кубика, который берется в данной
    итерации должен быть меньше или равен размеру верхнего кубика в башне.

    [4, 3, 2, 1, 3, 4] -> Yes -> 4>4>3>3>2>1
    [1, 3, 2] -> No
    """

    cubes_row = arr[:]
    tower_top_cube = cubes_row.pop(0) if cubes_row[0] >= cubes_row[-1] else cubes_row.pop(-1)

    for i in range(len(cubes_row)):
        if cubes_row[0] >= cubes_row[-1]:
            if cubes_row[0] <= tower_top_cube:
                tower_top_cube = cubes_row.pop(0)
            else:
                print('No')
                return
        elif cubes_row[0] < cubes_row[-1]:
            if cubes_row[-1] <= tower_top_cube:
                tower_top_cube = cubes_row.pop(-1)
            else:
                print('No')
                return

    print('Yes')


if __name__ == '__main__':
    cubes = list(map(int, input().split()))
    piling_up(cubes)

    # piling_up([1, 3, 2])  # -> No
    # piling_up([4, 3, 2, 1, 3, 4])  # -> Yes
    # piling_up([1, 2, 3, 8, 7])  # -> No
    # piling_up([1, 2, 3, 7, 8])  # -> Yes
