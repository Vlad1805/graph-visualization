# Copyright 2021 Stanciu Vlad

BFS visualization tool allows you to see the initial graph and the result of
the BFS traversal for a directed, connected, weighted graph given by the user input
file.

# input

The format for the input file is as follows:
n (number of edges) -> integer
n * n adjency matrix, with one line / row => n lines with n integers each,
		      where a(i, j) != 0 if there is an edge from node i to node j
		      and a(i, j) = 0 otherwise
      -> integer matrix
start_node (node from which you begin the traversal) -> integer
Keep in mind that the weight doesn't matter for BFS treversal.

# implementation

BFS function is implemented interatively, using color_map as visited array. The colors
are used to represent the distance from start node. Start is always green. Nodes on
odd levels (distance % 2 == 1) are blue and nodes on even levels are red.

Modules used:
-networkx -> graph manipulation and support for visualization
-matplotlib.pyplot -> plotting

# output

Left: initial graph
Right: BFS graph where node name is replaced with the distance from start