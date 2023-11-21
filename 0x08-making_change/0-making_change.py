#!/usr/bin/python3
"""determines the fewest number of coins needed to meet a given amount"""


def makeChange(coins, total):
    """
    Function to take a list of coins and use
       that to calculate how much change the total will require
    """
    if total <= 0:
        return 0

    # Initialize an array mc to store minimum number of coins for each amount
    else:
        coin = sorted(coins)
        coin.reverse()
        amount = 0

        # Update the array mc for each coin denomination
        for mc in coin:
            while(total >= mc):
                amount += 1
                total -= mc
        if total == 0:
            return amount
        return -1
