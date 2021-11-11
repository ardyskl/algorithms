#!/usr/bin/env python3
# coding: UTF-8
# The following code implements the Floyd-Warshall algorithm to solve all-pairs shortest paths problem. The algorithm can either
# find the shortest path of all paris or detect a negative cycle.

import math
import random

def read_clauses(filename):
    # read the 2SAT probelm from txt file
    with open(filename) as f:
        lines = f.readlines()
        n = int(lines[0])
        clauses = [[int(line.split()[0]), int(line.split()[1])]for line in lines[1:]]

    return clauses, n

def check_true(clauses, i, x):
    # check ig two clauses are satisfied
    x1 = not x[-clauses[i][0]] if clauses[i][0] < 0 else x[clauses[i][0]]
    x2 = not x[-clauses[i][1]] if clauses[i][1] < 0 else x[clauses[i][1]]
    return x1 or x2

def twoSat(clauses, n):
    # Papadimitriou's 2SAT algorithm main function
    length = len(clauses)
    for _ in range(int(math.log(length, 2))):
        x = [True] + [random.choice([True, False]) for _ in range(n)]
        for _ in range(2 * length ** 2):
            for j in range(length):
                if not check_true(clauses, j, x):
                    break
            if  check_true(clauses, j, x):
                return 1
            else:
                # random flip one boolean variable
                idx = random.randint(0, 1)
                x[abs(clauses[j][idx])] = not x[abs(clauses[j][idx])]
    return 0

def reduce_size(clauses):
    """ reduce the size of clauses
        If one variable only appears as either positive or negative, this clause can be removed as we can easily
        satisfy this clause by setting this variable always true or false.
        Iteratively remove these clauses to reduce the problem size
    """
    pos = {clause[0] for clause in clauses if clause[0] > 0} | {clause[1] for clause in clauses if clause[1] > 0}
    neg = {-clause[0] for clause in clauses if clause[0] < 0} | {-clause[1] for clause in clauses if clause[1] < 0}
    # use symmetic difference b/w two sets to determine the singular variables
    diff = pos.symmetric_difference(neg)
    while len(diff):
        i = 0
        while i < len(clauses):
            if abs(clauses[i][0]) in diff or abs(clauses[i][1]) in diff:
                clauses.pop(i)
            i += 1
        pos = {clause[0] for clause in clauses if clause[0] > 0} | {clause[1] for clause in clauses if clause[1] > 0}
        neg = {-clause[0] for clause in clauses if clause[0] < 0} | {-clause[1] for clause in clauses if clause[1] < 0}
        diff = pos.symmetric_difference(neg)
    return clauses

def main():
    # testing
    clauses, n = read_clauses('2sat_test.txt')
    clauses = reduce_size(clauses)
    print(twoSat(clauses, n))
    # running on main data dumps
    print('====running on 2sat1, 2, 3, 4, 5, 6.txts====')
    clauses, n = read_clauses('2sat1.txt')
    clauses = reduce_size(clauses)
    print(twoSat(clauses, n))
    clauses, n = read_clauses('2sat2.txt')
    clauses = reduce_size(clauses)
    print(twoSat(clauses, n))
    clauses, n = read_clauses('2sat3.txt')
    clauses = reduce_size(clauses)
    print(twoSat(clauses, n))
    clauses, n = read_clauses('2sat4.txt')
    clauses = reduce_size(clauses)
    print(twoSat(clauses, n))
    clauses, n = read_clauses('2sat5.txt')
    clauses = reduce_size(clauses)
    print(twoSat(clauses, n))
    clauses, n = read_clauses('2sat6.txt')
    clauses = reduce_size(clauses)
    print(twoSat(clauses, n))

if __name__ == '__main__':
    main()
