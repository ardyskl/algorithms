#!/usr/bin/env python3
# coding: UTF-8

#==========================================
# week 4, Course 1: Divide and conqure, Stanford algorithm specialization
#===========================================
# Thanks to Shuo Han (https://github.com/sh2439) for this short and efficient code
# compiled by ardy

# Please see and understand all the lectures before going through this solution

# A contraction algrothim is used to compute the minimum cut of a connected graph for example Karger's
# Contraction algorithms repeatedly contracts random edges in the graph, until only two nodes remain

'''
A cut (S,T) in an undirected graphG=(V,E) is a partition V
of the vertices into two non-empty, disjoint sets
{S (lies in) T = V}
'''

#TASK
'''
Your task is to code up and run the randomized contraction algorithm
for the min cut problem and use it on the above graph to compute the min cut.
(HINT: Note that you'll have to figure out an implementation of edge contractions.
Initially, you might want to do this naively, creating a new graph from the old every
time there's an edge contraction.  But you should also think about more
efficient implementations.)
'''

# WARNING:
'''
As per the video lectures, please make sure to run the algorithm many times with different random seeds
and remember the smallest cut that you ever find.
'''

import random
import copy
import sys
import traceback
import math

def main():
    try:

        # Change the file here to run on your own graph dump
        # import & include os.path if file not in working directory
        def read_file(name):

            with open('kargerMinCut.txt', 'r') as data:
                line = data.read().strip(). split("\n")

            graph_dictionary = {}
            for element in line:
                line_list = list(map(int, element.strip().split("\t")))
                graph_dictionary[line_list[0]] = line_list[1:]

            return graph_dictionary

        # Returns a randomly selected pair a and b
        def randomise(new_dict):

            a = random.choice(list(new_dict.keys()))
            b = random.choice(new_dict[a])

            selected_pair = (a, b)
            return selected_pair

        # Computes and returns a minimum cut in a single loop
        def karger(new_dict):

            num = []

            while len(new_dict) > 2:
                a, b = randomise(new_dict)
                # merge the vertices
                new_dict[a].extend(new_dict[b])

                # add a /delete b in vertices connected with b
                for c in new_dict[b]:
                    new_dict[c].remove(b)
                    new_dict[c].append(a)

                # Delete self loops of a vertice a
                while a in new_dict[a]:
                    new_dict[a].remove(a)

                # delete vertice b
                del new_dict[b]

            for key in new_dict:
                num.append(len(new_dict[key]))
            return num[0]

        def combine(n, name):
            #name = "kargerMinCut.txt"
            graph = read_file(name)
            min_cut = 1000
            for i in range(n):
                G = copy.deepcopy(graph)
                cut = karger(G)
                if cut < min_cut:
                    min_cut = cut
                    #if(min_cut < 20):
                    #break
            return min_cut

        # Driver code
        print("Karger algrothim")

        cont = "y"
        while(cont.lower() == "y"):

            choice = str(input("Want to test? [y/n]: "))

            if choice == 'n':
                print("==== Exiting ====")
                sys.exit(0)

            elif choice == 'y':
                print("\n=========running on kargerMinCut.txt=========")
                n = 1000
                name = "kargerMinCut.txt"
                print("Smallest cut:", combine(n, name))
                # comment break to test multiple times with different random seeds
                # More than 1 trials; for loop within combine() keeps iterating and priting smallet cuts for random values of a and b in kargerMinCut.txt
                break

        sys.exit(0)

    except KeyboardInterrupt:
        print("\n--- Shutdown requested exiting ---")
        quit()

    except Exception:
        traceback.print_exc(file=sys.stdout)
        sys.exit(0)

if __name__ == "__main__":
    main()
