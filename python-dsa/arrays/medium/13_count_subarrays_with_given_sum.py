def count_subarrays_with_given_sum(arr: list[int], target: int) -> int:
    count = 0
    prefix_sum = 0
    frequencies = {0: 1}

    for num in arr:
        prefix_sum += num
        count += frequencies.get(prefix_sum - target, 0)
        frequencies[prefix_sum] = frequencies.get(prefix_sum, 0) + 1

    return count


if __name__ == "__main__":
    sample = [3, 1, 2, 4]
    target = 6
    print("Subarray count:", count_subarrays_with_given_sum(sample, target))
