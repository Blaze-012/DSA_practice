def set_matrix_zeroes(matrix: list[list[int]]) -> list[list[int]]:
    rows = set()
    cols = set()

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                rows.add(row)
                cols.add(col)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row in rows or col in cols:
                matrix[row][col] = 0

    return matrix


if __name__ == "__main__":
    sample = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print("Matrix after zeroing:", set_matrix_zeroes(sample))
