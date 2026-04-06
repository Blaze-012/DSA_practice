def longest_consecutive_sequence(arr: list[int]) -> int:
    values = set(arr)
    longest = 0

    for num in values:
        if num - 1 not in values:
            current = num
            length = 1

            while current + 1 in values:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


if __name__ == "__main__":
    sample = [100, 4, 200, 1, 3, 2]
    print("Longest consecutive length:", longest_consecutive_sequence(sample))
