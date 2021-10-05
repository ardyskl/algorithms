#!/usr/bin/env python3
# coding: UTF-8

#==========================================
# week 3, Course 3: Greedy algorithms & Dynamic programming, Stanford algorithm specialization
#===========================================
# Thanks to anmourchen (https://github.com/anmourchen) for this short and efficient code
# compiled by ardy

# Dynamic programming
# We'll implementa dynamic programming algorithm for computing a maximum-weight independent set of a path graph
# Please see and understand all the lectures before going through this solution

# TASK
'''
Your task in this problem is to run the dynamic programming algorithm and the reconstruction procedure) from lecture on this data set.
The question is: of the vertices 1, 2, 3, 4, 17, 117, 517, and 997, which ones belong to the maximum-weight independent set?
(By "vertex 1" we mean the first vertex of the graph---there is no vertex 0. You should return a 8-bit string.
where the ith bit should be 1 if the ith of these 8 vertices is in the maximum-weight independent set, and 0 otherwise.
'''

'''
Integer/graph dumbs mwis_small.txt and mwis.txt, use your own place them
in the same directory
'''

import sys
import traceback
import math

def read_graph(filepath):
    with open(filepath) as f:
        lines = f.readlines()
        num = [int(line.split()[0]) for line in lines[1:]]
    return num

def mwis(num):
    W = [0] * (len(num) + 1)
    W[1] = num[0]
    for i in range(2, len(num) + 1):
        W[i] = max(W[i - 1], W[i - 2] + num[i - 1])

    S = []
    i = len(num)
    while i > 0:
        if W[i] > W[i - 2] + num[i - 1]:
            i -= 1
        else:
            S.append(i)
            i -= 2

    return W[len(num)], S

def main():
    # test case
    print("====Testing===")
    num = read_graph('mwis_small.txt')
    _, vertices = mwis(num)
    candidates = [9, 3, 4, 6]
    s = ['1' if i in vertices else '0' for i in candidates]
    print(''.join(s))
    print("---test case success!---")

    print("\n====running on mwis.txt====")
    num = read_graph('mwis.txt')
    _, vertices = mwis(num)
    candidates = [1, 2, 3, 4, 17, 117, 517, 997]
    s = ['1' if i in vertices else '0' for i in candidates]
    print(''.join(s))


if __name__ == '__main__':
    main()
