def min_coins(coins, target, current_count=0, min_count=float('inf')):
    # Base case: exact amount of change achieved
    if target == 0:
        return min(current_count, min_count)
    # Base case: no more coins or target becomes negative
    if not coins or target < 0:
        return min_count

    # Recursive case: for each coin, choose to use it or not
    for i in range(len(coins)):
        coin = coins[i]
        remaining_coins = coins[i:]
        # Choose to use the coin
        new_count = current_count + 1
        new_target = target - coin
        min_count = min_coins(remaining_coins, new_target, new_count, min_count)
        # Choose not to use the coin
        min_count = min_coins(remaining_coins, target, current_count, min_count)

    return min_count
