#!/usr/bin/env python3
# coding: UTF-8

#==========================================
# week 3, Course 2: Graph theory, Stanford algorithm specialization
#===========================================
# Thanks to anmourchen (https://github.com/anmourchen) for this short and efficient code
# compiled by ardy

# Please see and understand all the lectures before going through this solution

# BST or binary search trees all the nodes follow
# 1. The value of the key of the left sub-tree is less than the value of its parent (root) node's key.
# 2. The value of the key of the right sub-tree is greater than or equal to the value of its parent (root) node's key.
#

# This algrothim finds the median using BST data structures with a linear running time of O(log(n)).

'''
#TASK

The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 3 lecture on heap applications).  The text file contains a list of the integers from 1 to 10000 in unsorted order; you should
treat this as a stream of numbers, arriving one by one.  Letting x down (i)
denote the ith number of the file, the kth median is defined as the median of the numbers
x down (1),....,x down (k). (So, if k is odd, then is m down (k) is
((k+1)/2)th smallest number among xdown(1),....,xdown(k) if k is even then m down
(k) is the (k2)th smallest numner among xdown(1),....,xdown(k)

'''

# TESTING

'''
change Median.txt & median_test.txt with your own data dumps
Place them in the same directory
'''

import heapq
from heapq import heappop, heappush

def read_file(filename):

    with open(filename) as f:
        nums = [int(line.split()[0]) for line in f]
    return nums

def find_medians(x, heap_low, heap_high):
    if len(heap_low) == 0:
        heappush(heap_low, -x)
    else:
        m = -heap_low[0]
        if x > m:
            heappush(heap_high, x)
            if len(heap_high) > len(heap_low):
                y = heappop(heap_high)
                heappush(heap_low, -y)
        else:
            heappush(heap_low, -x)
            if len(heap_low) > len(heap_high) + 1:
                y = -heappop(heap_low)
                heappush(heap_high, y)

    return -heap_low[0]

def main():

    #testing
    nums = read_file('median_test.txt')
    heap_low, heap_high = [], []
    median_sum = sum([find_medians(num, heap_low, heap_high) for num in nums]) % 10000
    print(median_sum)

    nums = read_file('Median.txt')
    heap_low, heap_high = [], []
    median_sum = sum([find_medians(num, heap_low, heap_high) for num in nums]) % 10000
    print(median_sum)

if __name__ == '__main__':
    main()
