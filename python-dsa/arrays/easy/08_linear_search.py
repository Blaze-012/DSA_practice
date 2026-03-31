def linear_search(arr: list[int], target: int) -> int:
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


if __name__ == "__main__":
    sample = [1, 2, 4, 5, 7]
    target = 5
    print(f"Index of {target}:", linear_search(sample, target))
