def union_of_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    i = 0
    j = 0
    union: list[int] = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            value = arr1[i]
            i += 1
        else:
            value = arr2[j]
            j += 1

        if not union or union[-1] != value:
            union.append(value)

    while i < len(arr1):
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union


if __name__ == "__main__":
    sample1 = [1, 1, 2, 3, 4, 5]
    sample2 = [2, 3, 4, 4, 5, 6]
    print("Union:", union_of_sorted_arrays(sample1, sample2))
