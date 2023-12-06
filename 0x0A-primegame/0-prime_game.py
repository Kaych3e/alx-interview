#!/usr/bin/python3
"""Choosing Prime Numbers"""


def primeNumbers(n):
    primes = []
    shuffled = [True] * (n + 1)
    for num in range(2, n + 1):
        if (shuffled[num]):
            primes.append(num)
            for i in range(num, n + 1, num):
                shuffled[i] = False
    return primes


def isWinner(x, nums):
    """
    Module to determine the winner of the game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primes = primeNumbers(nums[i])
        if len(primes) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
