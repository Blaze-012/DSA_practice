def search_insert_position(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == "__main__":
    sample = [1, 3, 5, 6]
    print("Insert position:", search_insert_position(sample, 5))
