def generate_pascals_triangle(rows: int) -> list[list[int]]:
    triangle: list[list[int]] = []

    for row in range(rows):
        current_row = [1] * (row + 1)
        for col in range(1, row):
            current_row[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
        triangle.append(current_row)

    return triangle


if __name__ == "__main__":
    print("Pascal's triangle:", generate_pascals_triangle(5))
