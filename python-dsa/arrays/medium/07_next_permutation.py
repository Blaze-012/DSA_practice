def next_permutation(arr: list[int]) -> list[int]:
    pivot = len(arr) - 2

    while pivot >= 0 and arr[pivot] >= arr[pivot + 1]:
        pivot -= 1

    if pivot >= 0:
        successor = len(arr) - 1
        while arr[successor] <= arr[pivot]:
            successor -= 1
        arr[pivot], arr[successor] = arr[successor], arr[pivot]

    left = pivot + 1
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


if __name__ == "__main__":
    sample = [1, 2, 3]
    print("Next permutation:", next_permutation(sample))
