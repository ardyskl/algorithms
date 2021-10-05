#!/usr/bin/env python3
# coding: UTF-8

#==========================================
# week 1, Course 3: Greedy algorithms & Dynamic programming, Stanford algorithm specialization
#===========================================
# # Thanks to anmourchen (https://github.com/anmourchen) for this short and efficient code
# compiled by ardy

# Please see and understand all the lectures before going through this solution
# Starting with an easy greedy algrothim for minimised weighted sum of completion

# TASK 1: Jobs scheduling based on diff (w - l)
'''
In this programming problem and the next you'll code up the greedy algorithms from lecture for minimizing the weighted sum of completion times..
Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of the difference (weight - length).  Recall from lecture that this algorithm is not always optimal.
IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with higher weight first.  Beware: if you break ties in a different way, you are likely to get the wrong answer.
You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.
'''

# TAKS 2: Jobs scheduling based on ratio
'''
For this problem, use jobs.txt or use your own integer data dump in same directory.
Your task now is to run the greedy algorithm that schedules jobs (optimally) in decreasing order of the ratio (weight/length).
In this algorithm, it does not matter how you break ties.  You should report the sum of
weighted completion times of the resulting schedule a positive int.
'''

# the Data sets for all 3 Tasks are small enough for a straightforward O(mn) implementation of the algrothims using heaps can speed up efficiency even more

import sys
import traceback
import threading
from datetime import date

def read_jobs(filename):
    #load the weight & length from text file
    with open(filename) as f:
        lines = f.readlines()
        n = int(lines[0].split('\n')[0])
        w = [int(line.split()[0]) for line in lines[1:]]
        c = [int(line.split()[1]) for line in lines[1:]]
        return n, w, c

def costs(n, w, l):
    # compute the weighted completed time of given weights and lengths
    cost = 0
    for i in range(n):
        cost += w[i] * sum(l[:i +1])
    return cost

def greedydifference(n, w, l):
    # sort the weights & lengths using difference
    diff = [wi - li for wi, li in zip(w, l)]
    diff_tuple = [(di, wi) for di, wi in zip(diff, w)]
    index = sorted(range(n), key=lambda k: diff_tuple[k], reverse=True)
    return [w[i] for i in index], [l[i] for i in index]

def greedyratio(n, w, l):
    # sort the weights & lengths using ratio
    ratio = [wi / li for wi, li in zip(w, l)]
    index = sorted(range(n), key=lambda k: ratio[k], reverse=True)
    return [w[i] for i in index], [l[i] for i in index]

def main():

    print("====Testing====")
    n, w, l = read_jobs('jobs_test.txt')
    greedy_w, greedy_l = greedydifference(n, w, l)
    print(costs(n, greedy_w, greedy_l))
    greedy_w, greedy_l = greedyratio(n, w, l)
    print(costs(n, greedy_w, greedy_l))

    print("\n====running on jobs.txt====")
    n, w, l = read_jobs('jobs.txt')
    greedy_w, greedy_l = greedydifference(n, w, l)
    #Task 1
    print("diff w - l:", costs(n, greedy_w, greedy_l))
    greedy_w, greedy_l = greedyratio(n, w, l)
    #Task 2
    print("ratio:", costs(n, greedy_w, greedy_l))

if __name__ == '__main__':
    main()
