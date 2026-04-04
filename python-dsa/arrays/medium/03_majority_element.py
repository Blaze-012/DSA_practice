def majority_element(arr: list[int]) -> int:
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


if __name__ == "__main__":
    sample = [2, 2, 1, 1, 1, 2, 2]
    print("Majority element:", majority_element(sample))
