def rotate_matrix_90_degrees(matrix: list[list[int]]) -> list[list[int]]:
    size = len(matrix)

    for row in range(size):
        for col in range(row + 1, size):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for row in matrix:
        row.reverse()

    return matrix


if __name__ == "__main__":
    sample = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Rotated matrix:", rotate_matrix_90_degrees(sample))
