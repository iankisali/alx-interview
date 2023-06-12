## 0x08. Making Change

Given a pile of coins of different values, the function determines the fewest number of coins needed to meet a given amount total.

- Prototype: `def makeChange(coins, total)`
- Return: fewest number of coins needed to meet `total`
    - If `total` is `0` or less, return `0`
    - If `total` cannot be met by any number of coins you have, return `-1`
- `coins` is a list of the values of the coins in possession
- The value of a coin will always be an integer greater than 0
- There is an infinite number of each denomination of coin in the list
