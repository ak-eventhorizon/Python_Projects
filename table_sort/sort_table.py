def sort_table():

    # INPUT block
    n, m = map(int, input().split())
    table = list()
    for i in range(n):
        table.append(list(map(int, input().split())))
    sort_key_k = int(input())

    # STUB block for debugging
    # table = [[1, 32, 190], [2, 35, 175], [3, 41, 188], [4, 26, 195], [5, 24, 176]]
    # sort_key_k = 1

    table_sorted_by_key = sorted(table, key=lambda x: x[sort_key_k])

    for i in table_sorted_by_key:
        print(' '.join(map(str, i)))


if __name__ == '__main__':
    sort_table()
