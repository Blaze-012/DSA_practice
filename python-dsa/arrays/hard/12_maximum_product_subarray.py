def maximum_product_subarray(arr: list[int]) -> int:
    max_product = arr[0]
    min_product = arr[0]
    result = arr[0]

    for num in arr[1:]:
        if num < 0:
            max_product, min_product = min_product, max_product

        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)
        result = max(result, max_product)

    return result


if __name__ == "__main__":
    sample = [2, 3, -2, 4]
    print("Maximum product:", maximum_product_subarray(sample))
