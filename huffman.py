#!/usr/bin/env python3
# coding: UTF-8

#==========================================
# week 3, Course 3: Greedy algorithms & Dynamic programming, Stanford algorithm specialization
#===========================================
# Thanks to anmourchen (https://github.com/anmourchen) for this short and efficient code
# compiled by ardy

# Huffman coding is used for data compression,
# Huffman code is a particular type of optimal prefix which results in lossless data compression
# Please see and understand all the lectures before going through this solution
# We'll implement Huffman coding to find maximum and minimum lenghts of an array where we know the count of total symbols/integers
# and the weight of each symbol/integer

# TASK
'''
Your task in this problem is to run the Huffman coding algorithm
and find out the maximum length of a codeword in the resulting Huffman code
'''

'''
Data/symbol dumbs huffman_small.txt and huffman.txt, use your own place them
in the same directory
'''

import sys
import traceback
import math
import heapq
import collections
from heapq import heapify, heappop, heappush
from collections import namedtuple

Node = namedtuple('Node', ('weight', 'index'))

def read_file(name):
    # Given path of huffman_small & huffman.txt
    tree = []

    file = open(name, 'r')
    data = file.readlines()
    for index, line in enumerate(data[1:]):
        item = line.split()
        tree.append(Node(int(item[0]), str(index)))

    heapq.heapify(tree)
    return tree

def combine(a, b):
    return Node(a.weight+b.weight, '+'.join([a.index, b.index]))

def huffman(tree):

    code_len = [0]*len(tree)
    while(len(tree) > 1):
        a = heapq.heappop(tree)
        b = heapq.heappop(tree)

        new_node = combine(a, b)
        heapq.heappush(tree, new_node)

        com = [int(item) for item in new_node.index.split('+')]
        for i in com:
            code_len[i] += 1

    return code_len

# Driver code
def main():
    print("====Testing====")
    tree = read_file('huffman_small.txt')
    codes = huffman(tree)
    print(min(codes), max(codes))
    print("----test case success!----")

    print("\n====running on huffman.txt====")
    tree = read_file('huffman.txt')
    codes = huffman(tree)
    print(min(codes), max(codes))

if __name__ == '__main__':
    main()


'''
def read_code(filename):
    # read the weights of each symbol from file
    # returns a python dictionary key, value pair of max and min coding length
    code = {}
    with open(filename) as f:
        lines = f.readline()
        for i, line in enumerate(lines[1:]):
            code[i] = [int(line.split()[0]), 0, 0]
    return code

def huffman(code):
    # computes the min & max coding l from given list of symbols
    # using heap to find two symbol with minimal weights
    weight = [[w[0], w[1], w[2]] for node, w in code.items()]
    heapify(weight)
    while len(weight) > 1:
        i, j = heappop(weight), heapop(weight)
        heappush(weight, [i[0] + j[0], 1 + min(i[1], j[1]), 1 + max(i[2], j[2])])
    return weight[0][1], weight[0][2]

# Driver code
def main():
    # test case
    print("====Testing=====")
    code = read_code('huffman_small.txt')
    print(huffman(code))
    print("----test case success!----")

if __name__ == '__main__':
    main()
'''
