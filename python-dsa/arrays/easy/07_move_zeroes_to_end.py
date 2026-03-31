def move_zeroes_to_end(arr: list[int]) -> list[int]:
    non_zero_index = 0

    for index in range(len(arr)):
        if arr[index] != 0:
            arr[non_zero_index], arr[index] = arr[index], arr[non_zero_index]
            non_zero_index += 1

    return arr


if __name__ == "__main__":
    sample = [1, 0, 2, 3, 0, 4, 0, 1]
    print("Array after moving zeroes:", move_zeroes_to_end(sample))
