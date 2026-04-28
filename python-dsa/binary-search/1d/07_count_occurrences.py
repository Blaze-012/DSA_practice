def count_occurrences(arr: list[int], target: int) -> int:
    def first_index() -> int:
        left = 0
        right = len(arr) - 1
        answer = -1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                answer = mid
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return answer

    def last_index() -> int:
        left = 0
        right = len(arr) - 1
        answer = -1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                answer = mid
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return answer

    first = first_index()
    if first == -1:
        return 0

    last = last_index()
    return last - first + 1


if __name__ == "__main__":
    sample = [2, 4, 6, 8, 8, 8, 11, 13]
    print("Occurrence count:", count_occurrences(sample, 8))
