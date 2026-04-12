def merge_sorted_arrays_without_extra_space(
    arr1: list[int], arr2: list[int]
) -> tuple[list[int], list[int]]:
    left = len(arr1) - 1
    right = 0

    while left >= 0 and right < len(arr2):
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break

    arr1.sort()
    arr2.sort()
    return arr1, arr2


if __name__ == "__main__":
    sample1 = [1, 4, 8, 10]
    sample2 = [2, 3, 9]
    print("Merged arrays:", merge_sorted_arrays_without_extra_space(sample1, sample2))
