def single_number(arr: list[int]) -> int:
    result = 0

    for num in arr:
        result ^= num

    return result


if __name__ == "__main__":
    sample = [4, 1, 2, 1, 2]
    print("Single number:", single_number(sample))
