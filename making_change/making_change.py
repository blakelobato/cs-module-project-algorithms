#!/usr/bin/python

import sys

def making_change(amount, denominations):
  combos = [0] * (amount + 1)
  combos[0] = 1
  # going through denominations:
  for i in range(len(denominations)):
    for j in range(len(combos)):
      if denominations[i] <= j:
        combos[j] += combos[(j - denominations[i])]#update
  return combos[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")