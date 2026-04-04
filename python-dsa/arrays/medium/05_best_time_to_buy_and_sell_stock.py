def max_profit(prices: list[int]) -> int:
    minimum_price = prices[0]
    best_profit = 0

    for price in prices[1:]:
        best_profit = max(best_profit, price - minimum_price)
        minimum_price = min(minimum_price, price)

    return best_profit


if __name__ == "__main__":
    sample = [7, 1, 5, 3, 6, 4]
    print("Maximum profit:", max_profit(sample))
