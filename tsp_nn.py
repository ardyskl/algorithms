#!/usr/bin/env python3
# coding: UTF-8

#==========================================
# week 3, Course 4: Solutions to shortest Paths Revisited, NP-Complete
#===========================================
# Thanks to anmourchen (https://github.com/anmourchen) for this short and efficient code
# compiled by ardy

# Please see and understand all the lectures before going through this solution
# The following code implements an algorithm that solves the Travelling salesman prboelm
# Also called TSP

# The travelling salesman problem asks the following question:
# "Given a list of cities and the distances between each pair of cities,
# what is the shortest possible route that visits each city exactly once and returns to the origin city?

# This algorithm is used heavly for routing directions on transport navagation systems.

#TASK:

# This is the nearest neighbor heuristic (nn) variation of tsp, works on larger graph dumps/data sets

# You should implement the nearest neighbor heuristic:
# Start the tour at the first city.
# Repeatedly visit the closest city that the tour hasn't visited yet.  In case of a tie, go to the closest city with the lowest index.  For example, if both the third and fifth cities have the same distance from the first city (and are closer than any other city), then the tour should begin by going from the first city to the third city.
# Once every city has been visited exactly once, return to the first city to complete the tour.

import sys
import math
# import combinations

def distance(cities, i, j):
    # computes the distance between cities i and j
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

def read_file(filename):
    # read cities data from txt
    cities = {}
    with open(filename) as f:
        lines = f.readlines()
        n = int(lines[0])
        for line in lines[1:]:
            cities[int(line.split()[0])] = [float(line.split()[1]), float(line.split()[2])]

    return cities, n

def tsp_nn(cities, n):
    # compute the shortest distance using nearest neighbor heuristic approach
    visited = [1]
    dst = 0
    while len(visited) < n:
        unvisited = set(range(1, n + 1)) - set(visited)
        min_dst, j = min([(distance(cities, visited[-1], j), j) for j in unvisited])
        dst += min_dst
        visited.append(j)

    return int(dst + distance(cities, visited[-1], 1))

def main():
    print("====Testing====")
    cities, n = read_file('nn_test.txt')
    print(tsp_nn(cities, n))

    print("====running on nn.txt====")
    cities, n = read_file('nn.txt')
    print(tsp_nn(cities, n))

if __name__ == '__main__':
    main()
