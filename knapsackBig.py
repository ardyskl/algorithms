#!/usr/bin/env python3
# coding: UTF-8

#==========================================
# week 4, Course 3: Greedy algorithms & Dynamic programming, Stanford algorithm specialization
#===========================================
# # Thanks to anmourchen (https://github.com/anmourchen) for this short and efficient code
# compiled by ardy

# Please see and understand all the lectures before going through this solution

# We'll implement a knapsack algorithm. The knapsack problem deals with combinatorial optimization: Given a set of items, each with a weight and a value,
# determine the number of each item to include in a collection so that the total weight is less than or equal to a given
# limit and the total value is as large as possible

# TASK 2
'''
You will implement the knapsack algorithm. You can assume that all numbers are positive.
You should assume that item weights and the knapsack capacity are integers.
Use the data on small knapsack_big.txt. This instance is so big that the straightforward iterative implemetation
uses an infeasible amount of time and space.  So you will have to be creative to compute an optimal solution.
One idea is to go back to a recursive implementation, solving subproblems --- and, of course, caching the results to avoid redundant work
--- only on an "as needed" basis.  Also, be sure to think about appropriate data structures for storing and looking up solutions to subproblems.
'''

'''
To use your own integer/data dumps put it in the same directory
'''

import sys
sys.setrecursionlimit(2 ** 20)

def read_file(filename):
    # read knapsack_big.txt & returns no. of itema, vlaues and weights
    # of each int
    with open(filename) as f:
        lines = f.readlines()
        w, n = int(lines[0].split()[0]), int(lines[0].split()[1])
        values = [int(line.split()[0]) for line in lines [1:]]
        weights = [int(line.split()[1]) for line in lines [1:]]

    return w, n, values, weights

def knapsackBig(values, weights, w, v):
    # solving big knapsack problem with recursively
    # diving into subprobelms
    if w <= 0:
        return 0
    if len(values) == 1:
        if weights[0] <= w:
            return values[0]
        else:
            return 0
    v1 = v.get((len(values[:-1]), w))
    if not v1:
        v1 = knapsackBig(values[:-1], weights[:-1], w, v)
        v[(len(values[:-1]), w)] = v1
    v2 = v.get((len(values[:-1]), w - weights[-1]))
    if not v2:
        v2 = knapsackBig(values[:-1], weights[:-1], w - weights[-1], v)
        v[(len(values[:-1]), w - weights[-1])] = v2
    if weights[-1] <= w:
        v2 = v2 + values[-1]
    else:
        v2 = 0
    return max(v1, v2)

def main():
    w, n, values, weights = read_file('knapsack_big.txt')
    v = {}
    # print("====running on knapsack_big.txt====")
    print(knapsackBig(values, weights, w, v))

if __name__ == '__main__':
    main()
