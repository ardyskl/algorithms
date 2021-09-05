#!/usr/bin/env python3
# coding: UTF-8

#==========================================
# week 3, Course 2: Graph theory, Stanford algorithm specialization
#===========================================
# Thanks to anmourchen (https://github.com/anmourchen) for this short and efficient code
# compiled by ardy

# Please see and understand all the lectures before going through this solution

# Dijkstra's algorithm is a simple way to finds the shortest distance or paths between nodes/vertices in a graph.
# Dijkstra uses the weights of the edges to find the path that minimises the total distance (weight) between the source node and all other nodes.
# For example road networks, oil pipelines. thanks to Edsger W. Dijkstra.

'''
Intresting fact: World wide web can be considered a graph with each and every page
as a vertice and a link as an edge so let m = web pages and n = links so a graph will exist
comprising the whole world wide web as G (m, n).

'''

'''
# TASK
Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex)
as the source vertex, and to compute the shortest-path distances between 1 and every other vertex of the graph.
If there is no path between a vertex v and vertex 1, we'll define the shortest-path distance between 1 and v to be 1000000
'''

'''
IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn)
O(mn) time implementation of Dijkstra's algorithm should work fine.
OPTIONAL: For those of you seeking an additional challenge, try implementing the heap-based version.
Note this requires a heap that supports deletions, and you'll probably need to maintain some
kind of mapping between vertices and their positions in the heap.
'''

import sys
import collections
from collections import defaultdict
import heapq
from heapq import heappop, heappush

def read_file(filename):

    graph = defaultdict(list)
    with open(filename) as f:
        for lines in f:
            line = lines.split()
            if line:
                node = int(line[0])
                heads = [int(ln.split(',')[0]) for ln in line[1:]]
                costs = [int(ln.split(',')[1]) for ln in line[1:]]
                graph[node] = [(head, cost) for head, cost in zip(heads, costs)]
    return graph

def dijkstra(graph, source, sink):

    queue, visited, mins = [(0, source, ())], set(), {source: 0}
    while queue:
        (cost, vertex, path) = heappop(queue)
        if vertex not in visited:
            visited.add(vertex)
            path = path + (vertex,)
            if vertex == sink:
                return cost, path

            for head, c in graph.get(vertex, ()):
                current_cost = mins.get(head, None)
                new_cost = cost + c
                if current_cost is None or new_cost < current_cost:
                    mins[head] = new_cost
                    heappush(queue, (new_cost, head, path))

    return 1000000, None

def main():

    graph = read_file("dijkstraTest.txt")
    costs = [dijkstra(graph, 1 ,v)[0] for v in range(1, 9)]
    print("Test success!", costs)

    print("\n=======running on dijkstraData.txt")
    graph = read_file("dijkstraData.txt")
    nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    costs = [dijkstra(graph, 1, node)[0] for node in nodes]
    print(costs)

if __name__ == '__main__':
    main()
