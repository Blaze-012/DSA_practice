def find_repeating_and_missing_number(arr: list[int]) -> tuple[int, int]:
    seen = set()
    repeating = -1

    for num in arr:
        if num in seen:
            repeating = num
            break
        seen.add(num)

    expected = set(range(1, len(arr) + 1))
    missing = (expected - set(arr)).pop()
    return repeating, missing


if __name__ == "__main__":
    sample = [3, 1, 2, 5, 3]
    print("Repeating and missing:", find_repeating_and_missing_number(sample))
