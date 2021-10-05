#!/usr/bin/env python3
# coding: UTF-8

#==========================================
# week 1, Course 4: Solutions to shortest Paths Revisited, NP-Complete
#===========================================
# Thanks to anmourchen (https://github.com/anmourchen) for this short and efficient code
# compiled by ardy

# Huffman coding is used for data compression,
# Huffman code is a particular type of optimal prefix which results in lossless data compression
# Please see and understand all the lectures before going through this solution
# We'll implement Huffman coding to find maximum and minimum lenghts of an array where we know the count of total symbols/integers
# and the weight of each symbol/integer

# TASK
def read_graph(filename):
    # reads the graph from data dumb
    graph = {}
    with open(filename) as f:
        lines = f.readlines()
        n, m = int(lines[0].split()[0]), int(lines[0].split()[1])
        for line in lines[1:]:
            graph[int(line.split()[0]), int(line.split()[1])] =int(line.split()[2])

    return graph, n

def bellman_ford(graph, s, n):
    # compute the single-source shortest distance with bellman_ford algorithm
    A = {}
    for v in range(1, n + 1):
        if v == s:
            A[0, v] = 0
        else:
            A[0, v] = float('inf')

    for i in range(1, n):
        for v in range(1, n + 1):
            A_temp = [A[i - 1, w] + graph[w, v] for w in range(1, n + 1) if (w, v) in graph]
            A[i, v] = min(A[i - 1, v], min(A_temp))

    # run BF one more time
    for v in range(1, n + 1):
        A_temp = [A[n - 1, w] + graph[w, v] for w in range(1, n + 1) if (w, v) in graph]
        A[n, v] = min(A[n - 1, v ], min(A_temp))

    for v in range(1, n + 1):
        if A[n, v] !=  A[n - 1, v]:
            return

    return min([A[n - 1, v] for v in range(1, n + 1)])

def all_pairs(graph, n):
    # find the minimum all pair shortest distance

    As = []
    for s in range(1, n + 1):
        dst = bellman_ford(graph, s, n)
        if dst is None:
            return 'NULL'
        else:
            As.append(dst)
    return min(As)

def main():
    print('===Testing===')
    g1, n1 = read_graph('g_test.txt')
    print(all_pairs(g1, n1))
    g2, n2 = read_graph('g2_test.txt')
    print(all_pairs(g2, n2))

    print('===running on g1, g2, g3.txts===')
    g1, n1 = read_graph('g1.txt')
    print(all_pairs(g1, n1))
    g2, n2 = read_graph('g2.txt')
    print(all_pairs(g2, n2))
    g3, n3 = read_graph('g3.txt')
    print(all_pairs(g3, n3))

if __name__ == '__main__':
    main()
