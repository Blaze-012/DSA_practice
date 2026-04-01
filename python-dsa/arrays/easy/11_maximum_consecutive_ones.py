def maximum_consecutive_ones(arr: list[int]) -> int:
    count = 0
    maximum = 0

    for num in arr:
        if num == 1:
            count += 1
            if count > maximum:
                maximum = count
        else:
            count = 0

    return maximum


if __name__ == "__main__":
    sample = [1, 1, 0, 1, 1, 1]
    print("Maximum consecutive ones:", maximum_consecutive_ones(sample))
