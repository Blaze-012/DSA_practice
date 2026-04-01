def find_missing_number(arr: list[int], n: int) -> int:
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


if __name__ == "__main__":
    sample = [1, 2, 4, 5]
    n = 5
    print("Missing number:", find_missing_number(sample, n))
