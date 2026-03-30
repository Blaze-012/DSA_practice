def largest_element(arr: list[int]) -> int:
    if not arr:
        raise ValueError("Array must not be empty.")

    largest = arr[0]
    for num in arr[1:]:
        if num > largest:
            largest = num
    return largest


if __name__ == "__main__":
    sample = [2, 5, 1, 3, 0]
    print("Largest element:", largest_element(sample))
