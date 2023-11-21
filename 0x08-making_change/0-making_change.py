#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize an array mc to store minimum number of coins for each amount
    # Initialize with a value greater than any possible solution
    mc = [float('inf')] * (total + 1)

    # Base case: 0 coins needed for total of 0
    mc[0] = 0

    # Update the array mc for each coin denomination
    for coin in coins:
        for amount in range(coin, total + 1):
            mc[amount] = min(mc[amount], mc[amount - coin] + 1)

    # If dp[total] is still the initial value, it means total cannot be met
    return mc[total] if mc[total] != float('inf') else -1
