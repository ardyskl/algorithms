#!/usr/bin/env python3
# coding: UTF-8

#==========================================
# week 1, Course 4: Solutions to shortest Paths Revisited, NP-Complete
#===========================================
# Thanks to anmourchen (https://github.com/anmourchen) for this short and efficient code
# compiled by ardy

# Please see and understand all the lectures before going through this solution
# We'll implement floyd warshall to find minimum all-pair shortest distance in a given graph
# graph dumbs are g1, g2, g3 txts

# Compliexity of floyd_warshall O(n^2) takes 1 hour to finish**

def read_graph(filename):
    # read the graph structure from txt file
    graph = {}
    with open(filename) as f:
        lines = f.readlines()
        n, m = int(lines[0].split()[0]), int(lines[0].split()[1])
        for line in lines[1:]:
            graph[int(line.split()[0]), int(line.split()[1])] = int(line.split()[2])

    return graph, n

def floyd_warshall(graph, n):

    A = {}
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                A[i, j] = 0
            elif (i, j) in graph:
                A[i, j] = graph[i, j]
            else:
                A[i, j] = float('inf')

    for k in range(1, n + 1):
        A_next = {}
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                for j in range(1, n + 1):
                    A_next[i, j] = min(A.get((i, j)), A.get((i, k)) + A.get((k, j)))
        A = A_next.copy()

    if check_negative_cycle(A, n):
        return 'NULL'
    else:
        return min(A.values())

def check_negative_cycle(A, n):
    # Check if it has a negative cycle
    for i in range(1, n + 1):
        if A.get((i, i)) < 0:
            return True
    return False

def main():
    print('===Testing===')
    g1, n1 = read_graph('g_test.txt')
    print(floyd_warshall(g1, n1))
    g2, n2 = read_graph('g2_test.txt')
    print(floyd_warshall(g2, n2))

    print('===running on g1, g2, g3.txts===')
    g1, n1 = read_graph('g1.txt')
    print(floyd_warshall(g1, n1))
    g2, n2 = read_graph('g2.txt')
    print(floyd_warshall(g2, n2))
    g3, n3 = read_graph('g3.txt')
    print(floyd_warshall(g3, n3))

if __name__ == '__main__':
    main()
