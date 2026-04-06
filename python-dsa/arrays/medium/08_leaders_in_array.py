def leaders_in_array(arr: list[int]) -> list[int]:
    leaders: list[int] = []
    current_leader = float("-inf")

    for num in reversed(arr):
        if num > current_leader:
            leaders.append(num)
            current_leader = num

    leaders.reverse()
    return leaders


if __name__ == "__main__":
    sample = [10, 22, 12, 3, 0, 6]
    print("Leaders:", leaders_in_array(sample))
