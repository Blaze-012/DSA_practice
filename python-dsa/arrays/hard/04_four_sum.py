def four_sum(arr: list[int], target: int) -> list[list[int]]:
    arr.sort()
    quadruplets: list[list[int]] = []
    length = len(arr)

    for first in range(length - 3):
        if first > 0 and arr[first] == arr[first - 1]:
            continue

        for second in range(first + 1, length - 2):
            if second > first + 1 and arr[second] == arr[second - 1]:
                continue

            left = second + 1
            right = length - 1

            while left < right:
                total = arr[first] + arr[second] + arr[left] + arr[right]

                if total == target:
                    quadruplets.append([arr[first], arr[second], arr[left], arr[right]])
                    left += 1
                    right -= 1

                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return quadruplets


if __name__ == "__main__":
    sample = [1, 0, -1, 0, -2, 2]
    print("4 sum quadruplets:", four_sum(sample, 0))
