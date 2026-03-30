def remove_duplicates(arr: list[int]) -> tuple[int, list[int]]:
    if not arr:
        return 0, []

    unique_index = 0

    for index in range(1, len(arr)):
        if arr[index] != arr[unique_index]:
            unique_index += 1
            arr[unique_index] = arr[index]

    new_length = unique_index + 1
    return new_length, arr[:new_length]


if __name__ == "__main__":
    sample = [1, 1, 2, 2, 2, 3, 3]
    length, unique_values = remove_duplicates(sample)
    print("New length:", length)
    print("Array after removing duplicates:", unique_values)
