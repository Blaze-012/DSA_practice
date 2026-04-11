def largest_subarray_sum_zero(arr: list[int]) -> int:
    prefix_sum = 0
    longest = 0
    first_seen = {0: -1}

    for index, num in enumerate(arr):
        prefix_sum += num

        if prefix_sum in first_seen:
            longest = max(longest, index - first_seen[prefix_sum])
        else:
            first_seen[prefix_sum] = index

    return longest


if __name__ == "__main__":
    sample = [15, -2, 2, -8, 1, 7, 10, 23]
    print("Largest zero-sum subarray length:", largest_subarray_sum_zero(sample))
