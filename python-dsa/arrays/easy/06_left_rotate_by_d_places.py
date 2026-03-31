def left_rotate_by_d_places(arr: list[int], d: int) -> list[int]:
    if not arr:
        return []

    d %= len(arr)
    return arr[d:] + arr[:d]


if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5, 6, 7]
    print("Array after left rotation by 2 places:", left_rotate_by_d_places(sample, 2))
