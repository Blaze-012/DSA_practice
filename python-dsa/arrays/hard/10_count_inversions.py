def count_inversions(arr: list[int]) -> int:
    def merge_sort(left: int, right: int) -> int:
        if left >= right:
            return 0

        mid = (left + right) // 2
        inversions = merge_sort(left, mid)
        inversions += merge_sort(mid + 1, right)
        inversions += merge(left, mid, right)
        return inversions

    def merge(left: int, mid: int, right: int) -> int:
        temp: list[int] = []
        i = left
        j = mid + 1
        inversions = 0

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                inversions += mid - i + 1
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= right:
            temp.append(arr[j])
            j += 1

        arr[left : right + 1] = temp
        return inversions

    return merge_sort(0, len(arr) - 1)


if __name__ == "__main__":
    sample = [5, 3, 2, 4, 1]
    print("Inversion count:", count_inversions(sample))
