def majority_element_ii(arr: list[int]) -> list[int]:
    candidate1 = None
    candidate2 = None
    count1 = 0
    count2 = 0

    for num in arr:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    result: list[int] = []
    limit = len(arr) // 3

    if arr.count(candidate1) > limit:
        result.append(candidate1)
    if candidate2 != candidate1 and arr.count(candidate2) > limit:
        result.append(candidate2)

    return result


if __name__ == "__main__":
    sample = [3, 2, 3]
    print("Majority elements:", majority_element_ii(sample))
