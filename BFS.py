#!/usr/bin/env python3
# coding: UTF-8

#==========================================
# week 1, Course: 2, Graph theory, Stanford algorithm specialization
#===========================================
# written by ardy

import traceback
import sys
from collections import defaultdict

# This script will be Object oriented
class Graph:

    # constructor
    def __init__(self):
        #default dict to store graph
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)

        queue = []

        queue.append(s)
        visited[s] = True

        while(queue):

            s = queue.pop(0)
            print(s, end = " ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

# Driver code
print("BFS algrothim")

cont = "y"
while(cont.lower() == "y"):

    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("BFS with starting point from node 2: ")
    g.BFS(2)
    print("")

    break
    sys.exit(0)

# choice = str(input("Want to use your own graph? [y/n]: "))

'''
    if choice == 'y':
        # Input edge of a directed graph node 1 --> node 2
            num1 = int(input("From vetrice: "))
            num2 = int(input("To vertice: "))
            g.addEdge(num1, num2)
            num3 = int(input("From vetrice: "))
            num4 = int(input("To vertice: "))
            g.addEdge(num1, num2)
            num5 = int(input("From vetrice: "))
            num6 = int(input("To vertice: "))
            g.addEdge(num1, num2)
            num7 = int(input("From vetrice: "))
            num8 = int(input("To vertice: "))
            g.addEdge(num1, num2)
            num9 = int(input("From vetrice: "))
            num10 = int(input("To vertice: "))
            g.addEdge(num1, num2)
            num11 = int(input("From vetrice: "))
            num12 = int(input("To vertice: "))
            g.addEdge(num1, num2)

            input = int(input("Enter starting point: "))
            print("BFS with starting point: ")
            g.BFS()
'''

    #elif choice == 'n':
        # =========================
        # Create a graph
        # change edges Here
