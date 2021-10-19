def sum_of_intervals(arr: list) -> int:
    ranges = list()
    for begin, end in arr:
        ranges += range(begin, end)
    return len(set(ranges))


if __name__ == '__main__':
    intervals1 = [[1, 4], [7, 10], [3, 5]]
    intervals2 = [[1, 2], [6, 10], [11, 15]]
    intervals3 = [[1, 5], [10, 20], [1, 6], [16, 19], [5, 11]]

    print(sum_of_intervals(intervals1))  # -> 7
    print(sum_of_intervals(intervals2))  # -> 9
    print(sum_of_intervals(intervals3))  # -> 19
