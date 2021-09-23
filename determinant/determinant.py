def determinant(matrix: list) -> int:
    """Determinant of 2d-matrix."""

    total = 0
    # Section 1: store indexes in list for row referencing
    indexes = list(range(len(matrix)))

    # Section 2: determinant of a 1x1 matrix yields the value of the one element
    if len(matrix) == 1:
        return matrix[0][0]

    # Section 3: when at 2x2 sub-matrix recursive calls end
    if len(matrix) == 2 and len(matrix[0]) == 2:
        result = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return result

    # Section 4: define sub-matrix for focus column and call this function
    for focus_column in indexes:
        # find the sub-matrix ...
        current_matrix = list(matrix)  # make a copy
        current_matrix = current_matrix[1:]  # remove the first row
        height = len(current_matrix)

        for i in range(height):
            # for each remaining row of sub-matrix remove the focus column elements
            current_matrix[i] = current_matrix[i][0:focus_column] + current_matrix[i][focus_column + 1:]

        sign = (-1) ** (focus_column % 2)
        # pass sub-matrix recursively
        sub_determinant = determinant(current_matrix)
        # total all returns from recursion
        total += sign * matrix[0][focus_column] * sub_determinant

    return total


# TESTS:

m0 = [[1]]  # 1x1
m1 = [[1, 3], [2, 5]]  # 2x2
m2 = [[2, 5, 3], [1, -2, -1], [1, 3, 4]]  # 3x3
m3 = [[2, 4, 7, 12], [-9, 5, 34, 1], [-9, -5, -3, 9], [2, 3, 12, -3]]  # 4x4

if __name__ == '__main__':
    print(determinant(m0))  # -> 1
    print(determinant(m1))  # -> -1
    print(determinant(m2))  # -> -20
    print(determinant(m3))  # -> -6578
