def reverse_pairs(arr: list[int]) -> int:
    def merge_sort(left: int, right: int) -> int:
        if left >= right:
            return 0

        mid = (left + right) // 2
        count = merge_sort(left, mid)
        count += merge_sort(mid + 1, right)
        count += count_pairs(left, mid, right)
        merge(left, mid, right)
        return count

    def count_pairs(left: int, mid: int, right: int) -> int:
        count = 0
        j = mid + 1

        for i in range(left, mid + 1):
            while j <= right and arr[i] > 2 * arr[j]:
                j += 1
            count += j - (mid + 1)

        return count

    def merge(left: int, mid: int, right: int) -> None:
        temp: list[int] = []
        i = left
        j = mid + 1

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= right:
            temp.append(arr[j])
            j += 1

        arr[left : right + 1] = temp

    return merge_sort(0, len(arr) - 1)


if __name__ == "__main__":
    sample = [40, 25, 19, 12, 9, 6, 2]
    print("Reverse pairs:", reverse_pairs(sample))
