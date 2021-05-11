# Copyright 2021 Popescu Silviu

Floyd Warshall's algorithm implementation, which enables the user to visualize the initial graph, alongside with a matrix that stores the minimum distances between each pair of two nodes. The graph is directed, connected, and weighted.

# input

The format for the input file is as follows:
n (number of edges) -> integer
n * n adjacency matrix, with one line / row => n lines with n integers each,
		      where a(i, j) != 0 if there is an edge from node i to node j
		      and a(i, j) = 0 otherwise
      -> integer matrix

# implementation

Floyd Warshall Algorithm is implemented iteratively, using a distance-matrix, which stores the minimum distance between each pair of two nodes.
If there is no path between two edges, then the distance-matrix would store INF(INF = the largest int number the system can hold)

Modules used:
-networkx -> graph manipulation and support for visualization
-matplotlib.pyplot -> plotting

# output

->initial graph plot
->distance matrix