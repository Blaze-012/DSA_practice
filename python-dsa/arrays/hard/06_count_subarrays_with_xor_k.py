def count_subarrays_with_xor_k(arr: list[int], target: int) -> int:
    count = 0
    prefix_xor = 0
    frequencies = {0: 1}

    for num in arr:
        prefix_xor ^= num
        count += frequencies.get(prefix_xor ^ target, 0)
        frequencies[prefix_xor] = frequencies.get(prefix_xor, 0) + 1

    return count


if __name__ == "__main__":
    sample = [4, 2, 2, 6, 4]
    print("Subarrays with XOR 6:", count_subarrays_with_xor_k(sample, 6))
