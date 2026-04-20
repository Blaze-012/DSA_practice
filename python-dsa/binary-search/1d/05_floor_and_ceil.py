def floor_and_ceil(arr: list[int], target: int) -> tuple[int, int]:
    floor_value = -1
    ceil_value = -1
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return arr[mid], arr[mid]
        if arr[mid] < target:
            floor_value = arr[mid]
            left = mid + 1
        else:
            ceil_value = arr[mid]
            right = mid - 1

    return floor_value, ceil_value


if __name__ == "__main__":
    sample = [3, 4, 4, 7, 8, 10]
    print("Floor and ceil:", floor_and_ceil(sample, 5))
