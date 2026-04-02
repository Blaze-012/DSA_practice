def longest_subarray_with_sum_k(arr: list[int], k: int) -> int:
    prefix_sum = 0
    longest = 0
    first_occurrence: dict[int, int] = {}

    for index, num in enumerate(arr):
        prefix_sum += num

        if prefix_sum == k:
            longest = index + 1

        remaining = prefix_sum - k
        if remaining in first_occurrence:
            longest = max(longest, index - first_occurrence[remaining])

        if prefix_sum not in first_occurrence:
            first_occurrence[prefix_sum] = index

    return longest


if __name__ == "__main__":
    sample = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
    k = 3
    print("Longest subarray length:", longest_subarray_with_sum_k(sample, k))
