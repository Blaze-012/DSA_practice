def is_sorted(arr: list[int]) -> bool:
    for index in range(1, len(arr)):
        if arr[index] < arr[index - 1]:
            return False
    return True


if __name__ == "__main__":
    sample = [1, 2, 2, 3, 4]
    print("Is sorted:", is_sorted(sample))
