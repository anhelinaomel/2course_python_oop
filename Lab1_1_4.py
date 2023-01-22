# You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
# There is only one instance of each bar and for each bar you can either take it or not (hence you cannot take a fraction of a bar).
# Write a function that returns the maximum weight of gold that fits into a knapsack's capacity.

import argparse

parser = argparse.ArgumentParser(description='Find max weight of gold that fits a bag')

parser.add_argument('-W',
                    required=True,
                    dest='capacity',
                    help='Knapsack\'s capacity',
                    type=int
                    )

parser.add_argument('-w',
                    dest='golden_bars',
                    help='List of golden_bars',
                    type=int,
                    nargs='+'
                    )

parser.add_argument('-n',
                    required=True,
                    dest='num',
                    help='Num of golden_bars',
                    type=int
                    )

args = parser.parse_args()

def max_weight(capacity, weights, bars_number):
    res = [[True] + [False] * capacity]    # list of all solutions (in rows)
    print(res)
    for i in range(bars_number):
        res.append(res[-1][:])             # copying previous row of solutions to update it with next golden bar info
        for w in range(weights[i], capacity + 1):
            res[-1][w] = res[-2][w] or res[-2][w - weights[i]]  # update row with new golden bar or with its sum with previous weights
        res = res[-1:]                                          # copying only last row
    for w in range(capacity, -1, -1):
        if res[-1][w]:                                          # get the last True as maximum weight
            return w

print(max_weight(args.capacity, args.golden_bars, args.num))
