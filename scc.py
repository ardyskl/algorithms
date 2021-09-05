#!/usr/bin/env python3
# coding: UTF-8

#==========================================
# week 1, Course 2: Graph theory, Stanford algorithm specialization
#===========================================
# Thanks to anmourchen (https://github.com/anmourchen) for this short and efficient code
# compiled by ardy

# Please see and understand all the lectures before going through this solution

# Vertices and nodes are the same
# Strongly connected components follow Depth first search(DSF) or Depth first traversal
# implemented in the DFS and DFS_loop1 functions

'''
In the mathematical theory of directed graphs, a graph is said to be
strongly connected if every vertex is reachable from every other vertex or node.
An SCC is called strongly connected components. DFS is used to search every vertice or nodes
to find out if the graphs is strongly connected and their sizes. SCC is a Depth first Search (DFS)
DFS of a graph with only one SCC always produces a tree.
'''

# TASK
'''
SCC.txt contains the edges of a directed graph. Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs),
and to run this algorithm on the given graph. You should output the sizes of the 5 largest SCCs.
'''

# TESTING
'''
Add your own integer dump or change scc_test.txt in the same directory, main results from SCC.txt data dump
'''

import sys
import traceback
import threading
import collections
from collections import defaultdict

class Track():

    def __init__(self):
        self.visited = set()
        self.current_time = 0
        self.current_source = []
        self.leader = defaultdict(list)
        self.finishing_times = {}

    def addNode(self, node):
        self.leader[self.current_source].append(node)

def read_file(filename):

    edges = []
    with open(filename) as f:
        for lines in f:
            line = lines.split()
            edges.append((int(line[0]), int(line[1])))

    nodes = list(set([v for edge in edges for v in edge]))
    graph  = {i: [] for i in range(1, len(nodes) +1)}
    graph_rev = {i: [] for i in range(1, len(nodes) +1)}
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph_rev[edge[1]].append(edge[0])

    return (graph, graph_rev, nodes)

def DFS(graph, start, track):
    track.visited.add(start)
    track.addNode(start)
    for v in graph[start]:
        if v in graph[start]:
            if v not in track.visited:
                DFS(graph, v, track)

    track.current_time += 1
    track.finishing_times[start] = track.current_time

def DFS_loop1(graph, nodes, track):
    for node in nodes:
        if node not in track.visited:
            track.current_source = node
            DFS(graph, node, track)

def scc(graph, graph_rev, nodes):
    track = Track()
    DFS_loop1(graph_rev, nodes, track)
    sorted_nodes = sorted(track.finishing_times, key=track.finishing_times.get, reverse=True)
    track = Track()
    DFS_loop1(graph, sorted_nodes, track)
    return track

def most_common(leader, x):
    results = [len(v) for k, v in leader.items()] + [0] * x
    return sorted(results, reverse=True)[: x]

def main():

    print("Finding 5 largest SCCs")

    cont = "y"
    while(cont.lower() == "y"):
        #=============================
        # User test case

        choice = str(input("Want to test? [y/n]: "))

        if choice == 'y':

            graph, graph_rev, nodes = read_file("scc_test.txt")
            track = scc(graph, graph_rev, nodes)
            print("\n", most_common(track.leader, 5))
            print("-----testing success!-------\n")

            print("=========running on SCC.txt=========")
            graph, graph_rev, nodes = read_file("SCC.txt")
            track = scc(graph, graph_rev, nodes)
            #print("5 largest SCCs:")
            print(most_common(track.leader, 5))
            sys.exit(0)

        elif choice == 'n':
            print("==== Exiting ====")
            sys.exit(0)

        #break

if __name__ == '__main__':
    # for 64MB stack
    threading.stack_size(67108864)
    # Around 1048576 recursions
    # use sys.getrecursionlimit() to get set limit
    # usually recursion limit is 1000 in python3
    sys.setrecursionlimit(2 ** 20)
    # instating thread object
    thread = threading.Thread(target=main)
    # running at target
    thread.start()
