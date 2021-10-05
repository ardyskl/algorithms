#!/usr/bin/env python3
# coding: UTF-8

#==========================================
# week 2, Course 3: Greedy algorithms & Dynamic programming, Stanford algorithm specialization
#===========================================
# # Thanks to anmourchen (https://github.com/anmourchen) for this short and efficient code
# compiled by ardy

# Please see and understand all the lectures before going through this solution
# This is an implementation of Kruskals MST algrothim

# TASK 1: In this programming problem and the next you'll code up the clustering algorithm from lecture for computing a max-spacing k-clustering

'''
Your task in this problem is to run the clustering algorithm from lecture on this data set, where the target number
k of clusters is set to 4.  What is the maximum spacing of a 4-clustering?
'''

'''
Kruskal's algorithm finds a minimum spanning forest of an undirected edge-weighted graph. It is a greedy algorithm in graph theory
as in each step it adds the next lowest-weight edge that will not form a cycle to the minimum spanning forest.
'''

import sys
import traceback
import threading
from collections import defaultdict
from itertools import combinations
from unionfind import UnionFind

def read_cluster(filename):
    # reads the graph structure from clustering1.txt
    # returns a list of tuples, 2 nodes & cost
    with open(filename) as f:
        lines = f.readlines()
        graph = [(int(line.split()[0]), int(line.split()[1]), int(line.split()[2])) for line in lines[1:]]
    return graph

def read_clusterbig(filename):
    # read the graph structure from clustering_big.txt
    # a python dicy {integer: line id}
    nodes = defaultdict(list)
    with open(filename) as f:
        lines = f.readlines()
        for i, line in enumerate(lines[1:]):
            num = int(''.join(line.split()), 2)
            nodes[num].append(i)
    return nodes

def hamming1(num):
    # returns the list of numbers with 1 bit different
    masks = [1 << i for i in range(num.bit_length())]
    code = [num ^ mask for mask in masks]
    return code

def hamming2(num):
    # returns the list of numbers with 1 bit different
    masks = [(1 << i) ^ (1 << j) for (i, j) in combinations(range(num.bit_length()), 2)]
    code = [num ^ mask for mask in masks]
    return code

def kclusteringB(nodes):
    # clustering nodes by hamming distance
    clusters = UnionFind(nodes)
    for num in nodes:
        # iterating thru hamming numbers
        for code in hamming1(num):
            if code in nodes:
                clusters.union(num, code)
        # iterating again thru hamming numbers
        for code in hamming2(num):
            if code in nodes:
                clusters.union(num, code)

    return len(clusters.subtree.keys())

def kclusteringS(graph, k):
    # computes the maximum spacing of the cluster
    nodes = set()
    for u, v, d in graph:
        nodes.add(u)
        nodes.add(v)

    group = UnionFind(nodes)
    # sort the graph by costs
    graph = sorted(graph, key=lambda x: x[2])

    while len(group.subtree.keys()) > k:
        u, v, d = graph.pop(0)
        group.union(u, v)

    # loop to stop returns the cost b/w two nodes that are both in same cluster
    while True:
        u, v, min_cost = graph.pop(0)
        if group.find(u) != group.find(v):
            break
    return min_cost

def main():

    choice = str(input("Choose data dump: [clustering1.txt or clustering_big.txt, use lowercase]: "))

    if choice == 'clustering1.txt':
        print("====running on clustering1.txt====")
        graph = read_cluster('clustering1.txt')
        print(kclusteringS(graph, 4))

    if choice == 'clustering_big.txt':
        print("====running on clustering_big.txt====")
        graph = read_clusterbig('clustering_big.txt')
        print(kclusteringB(graph))
        sys.exit(0)

    if choice not in 'clustering1.txt' and 'clustering_big.txt':
        print("Please choose a data dump or use you own")
        sys.exit(0)

if __name__ == '__main__':
    main()
