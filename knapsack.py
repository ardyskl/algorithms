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

# TASK 1
'''
You will implement the knapsack algorithm from lectures, You can assume that all numbers are positive.
You should assume that item weights and the knapsack capacity are integers.
Use the data on small knapsack1.txt
'''

'''
Use your own integer/data dumps put it in the same directory
'''

import sys
import traceback
import math

def read_file(filename):
    # reads data in the file
    # returns capacity, number of items, values & weights of each integer
    with open(filename) as f:
        lines = f.readlines()
        w, n = int(lines[0].split()[0]), int(lines[0].split()[1])
        values = [int(line.split()[0]) for line in lines [1:]]
        weights = [int(line.split()[1]) for line in lines [1:]]

    return w, n, values, weights

def knapsack(w, n, values, weights):
    v = [[0 for i in range(w + 1)] for j in range(n +1)]

    for i in range(1, n + 1):
        for x in range(0, w + 1):
            if x < weights[i - 1]:
                v[i][x] = v[i - 1][x]
            else:
                v[i][x] = max(v[i - 1][x], v[i - 1][x - weights[i - 1]] + values[i - 1])
    return v[n][w]

def main():
    w, n, values, weights = read_file('knapsack1.txt')
    print("====running on knapsack1.txt====")
    print(knapsack(w, n, values, weights))

if __name__ == '__main__':
    main()
