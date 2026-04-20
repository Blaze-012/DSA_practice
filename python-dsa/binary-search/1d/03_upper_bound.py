def upper_bound(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == "__main__":
    sample = [1, 2, 2, 3, 5]
    print("Upper bound index:", upper_bound(sample, 2))
