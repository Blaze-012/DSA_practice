def three_sum(arr: list[int]) -> list[list[int]]:
    arr.sort()
    triplets: list[list[int]] = []

    for index in range(len(arr) - 2):
        if index > 0 and arr[index] == arr[index - 1]:
            continue

        left = index + 1
        right = len(arr) - 1

        while left < right:
            total = arr[index] + arr[left] + arr[right]

            if total == 0:
                triplets.append([arr[index], arr[left], arr[right]])
                left += 1
                right -= 1

                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return triplets


if __name__ == "__main__":
    sample = [-1, 0, 1, 2, -1, -4]
    print("3 sum triplets:", three_sum(sample))
