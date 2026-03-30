def second_largest(arr: list[int]) -> int:
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements.")

    largest = float("-inf")
    second = float("-inf")

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num

    if second == float("-inf"):
        raise ValueError("Second largest element does not exist.")

    return int(second)


if __name__ == "__main__":
    sample = [1, 2, 4, 7, 7, 5]
    print("Second largest element:", second_largest(sample))
