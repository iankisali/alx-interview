#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """Given a pile of coins of different values,
    determining fewest num of coins needed to meet a given amount total"""
    if total <= 0:
        return 0
    pile = [0] + [float("inf")] * (total)
    for coin in coins:
        for x in range(coin, total + 1):
            pile[x] = min(pile[x], pile[x - coin] + 1)
    return pile[-1] if pile[-1] != float("inf") else -1
