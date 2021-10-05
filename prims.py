#!/usr/bin/env python3
# coding: UTF-8

#==========================================
# week 1, Course 3: Greedy algorithms & Dynamic programming, Stanford algorithm specialization
#===========================================
# # Thanks to anmourchen (https://github.com/anmourchen) for this short and efficient code
# compiled by ardy

# Please see and understand all the lectures before going through this solution
# We'll implement Prims minimum spanning tree algorithm, also known as Jarník's algorithm
# Prims used for finding the MST or minimum spanning tree for a weighted undirected graph
# The total weight of all edges in the tree is minimised

# TASK 3: Jobs scheduling
'''
Your task is to run Prim's minimum spanning tree algorithm on this graph.
You should report the total cost of a minimum spanning tree --- an integer,
which may or may not be negative.
'''
# the Data sets for all 3 Tasks are small enough for a straightforward O(mn) implementation of the algrothims using heaps can speed up efficiency even more

import sys
import traceback

def load_graph(file):
    # Loads the graph
    graph = {}
    nodes = set()
    with open(file) as f:
        lines = f.readlines()
        for line in lines[1:]:
            v1 = int(line.split()[0])
            v2 = int(line.split()[1])
            c = int(line.split()[2])
            graph[(v1, v2)] = c
            nodes.add(v1)
            nodes.add(v2)
    return graph, nodes

def MST(graph, nodes):
    # Prims implementation
    span = {list(nodes)[0]}
    cost = []
    while span != nodes:
        min_cost = float("inf")
        for v1 in span:
            for v2 in nodes - span:
                if (v1, v2) in graph and graph[(v1, v2)] < min_cost:
                    node = v2
                    min_cost = graph[(v1, v2)]
                if (v2, v1) in graph and graph[(v2, v1)] < min_cost:
                    node = v2
                    min_cost = graph[(v2, v1)]
        span.add(node)
        cost.append(min_cost)
    return sum(cost)

def main():
    print("====Testing====")
    graph, nodes = load_graph('edges_test.txt')
    print(MST(graph, nodes))
    
    print("====running on edges.txt====")
    graph, nodes = load_graph('edges.txt')
    print(MST(graph, nodes))

if __name__ == '__main__':
    main()
