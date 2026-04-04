def maximum_subarray_sum(arr: list[int]) -> int:
    current_sum = arr[0]
    best_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)

    return best_sum


if __name__ == "__main__":
    sample = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Maximum subarray sum:", maximum_subarray_sum(sample))
