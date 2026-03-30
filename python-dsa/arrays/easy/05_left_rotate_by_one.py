def left_rotate_by_one(arr: list[int]) -> list[int]:
    if not arr:
        return []

    first_element = arr[0]
    for index in range(1, len(arr)):
        arr[index - 1] = arr[index]
    arr[-1] = first_element
    return arr


if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5]
    print("Array after left rotation by one:", left_rotate_by_one(sample))
