def two_sum(arr: list[int], target: int) -> tuple[int, int] | None:
    seen: dict[int, int] = {}

    for index, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return seen[complement], index
        seen[num] = index

    return None


if __name__ == "__main__":
    sample = [2, 6, 5, 8, 11]
    target = 14
    print("Two sum indices:", two_sum(sample, target))
