def rearrange_array_by_sign(arr: list[int]) -> list[int]:
    positives = []
    negatives = []

    for num in arr:
        if num >= 0:
            positives.append(num)
        else:
            negatives.append(num)

    result: list[int] = []
    for index in range(len(positives)):
        result.append(positives[index])
        result.append(negatives[index])

    return result


if __name__ == "__main__":
    sample = [3, 1, -2, -5, 2, -4]
    print("Rearranged array:", rearrange_array_by_sign(sample))
