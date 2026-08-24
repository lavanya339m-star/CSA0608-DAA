def insert_price(prices, new_price):
    low = 0
    high = len(prices)
    while low < high:
        mid = (low + high) // 2
        if prices[mid] < new_price:
            low = mid + 1
        else:
            high = mid
    prices.append(0)
    i = len(prices) - 1
    while i > low:
        prices[i] = prices[i - 1]
        i -= 1
    prices[low] = new_price
    return prices
prices = []
for p in [102.5, 98.3, 105.1, 100.0, 97.8]:
    prices = insert_price(prices, p)
assert prices == sorted([102.5, 98.3, 105.1, 100.0, 97.8])
assert prices[0] == min(prices) and prices[-1] == max(prices)
print("All test cases passed!")
print("Sorted prices:", prices)
print("Minimum price:", prices[0])
print("Maximum price:", prices[-1])
