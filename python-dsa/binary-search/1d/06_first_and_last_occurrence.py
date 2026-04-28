def first_and_last_occurrence(arr: list[int], target: int) -> tuple[int, int]:
    def find_first() -> int:
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

    def find_last() -> int:
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

    return find_first(), find_last()


if __name__ == "__main__":
    sample = [2, 4, 6, 8, 8, 8, 11, 13]
    print("First and last occurrence:", first_and_last_occurrence(sample, 8))
