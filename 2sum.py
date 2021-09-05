#!/usr/bin/env python3
# coding: UTF-8

#==========================================
# week 4, Course 2: Graph theory, Stanford algorithm specialization
#===========================================
# # Thanks to anmourchen (https://github.com/anmourchen) for this short and efficient code
# compiled by ardy

# Please see and understand all the lectures before going through this solution

# The 2SUM problem is a challenge to find all the pairs of two integers in an unsorted array that sum up to a given S
# this algrothim has a running time of o(n^2) which is not the best and takes around 2 hours to find the target values

'''
Array can have non-positive integers
If arr = [2,5,8,3,-2,9,0] We need to find the number combinations that we’ll equal 3, our “targetSum”.

#TASK

Your task is to compute the number of target values t in the interval [-10000,10000]
(inclusive) such that there are distinct numbers x, y in the input file that satisfy
x + y = t. (NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)
'''

# TESTING

'''
Tested on MacBook Air M1 2020, 2 hours to finish if running on programming_prob-2sum.txt data dump
Change the main fucntion to use your own data dumps
'''

import sys
import traceback
import threading
import tqdm
from tqdm import tqdm

# We will implement the hashtable version
# hashtable is a simple dictionary
hashtable = {}

# Reading .txt integer dumb
def read_nums(filename):
    with open(filename) as f:
        lines = f.readlines()
    nums = [int(line.split()[0]) for line in lines]
    for num in nums:
        hashtable[num] = 1
    return nums

def twoSum(nums, low, high):
    # implementation of the main algo function
    # finds the counts of a target in low, end that satsfies sum of two
    # elements in the nums = target
    # Still taking 3 hours?
    count = 0
    for target in tqdm(range(low, high + 1)):
        tmp_dict = hashtable.copy()
        for num in nums:
            if num in hashtable and target - num in tmp_dict and num != target - num:
                count += 1
                break
    return count

# Driver code
def main():
    # testing 1
    print("Test1")
    nums = read_nums('2sum_test.txt')
    count = twoSum(nums, 9, 11)
    print(count)

    # testing 2
    print("====running on assignmentIntegers dump====")
    # running on big integer dump
    nums = read_nums('programming_prob-2sum.txt')
    count = twoSum(nums, -10000, 10000)
    print(count)

if __name__ == '__main__':
    thread = threading.Thread(target=main)
    thread.start()
