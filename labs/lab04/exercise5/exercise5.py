def find_momentum_days(prices):
    momentum_days = []
    for i in range( len(prices)):
        today_change = prices[i] - prices[i - 1]
        previous_change = prices[i - 1] - prices[i - 2]

    if today_change > 0 and today_change > previous_change:
        momentum_days.append(i)
    return momentum_days

# Test
prices = [100, 102, 105, 107, 106, 108, 112, 114]
result = find_momentum_days(prices)
print(f"Momentum days: {result}")  # Expected: [2, 5, 6]
