# Copyright 2021 Stanciu Vlad

Dijkstra visualization tool allows you to see the initial graph and the result of
the Dijkstra shortest path for a directed, connected, weighted graph given by the user
using an input file.

# input

The format for the input file is as follows:
n (number of edges) -> integer
n * n adjacency matrix, with one line / row => n lines with n integers each,
		      where a(i, j) != 0 if there is an edge from node i to node j
		      and a(i, j) = 0 otherwise
      -> integer matrix
start_node (node from which you begin the traversal) -> integer
Keep in mind that the weight doesn't matter for Dijkstra treversal.

# implementation

Dijkstra function is implemented interatively.

In each iteration we look for the node u that has the smallest cost from start
using the MinDistance function. (keep in mind that the smallest cost is not
always achieved with one edge, sometimes it can be obtained through multiple edges).
Next we check if all the other nodes have a better cost if we connect them
to start from a different route that goes through the node returned from MinDistance.
We mark u as "visited" (sptSet[u] = True) so we don't check the same node twice.
Now we determine the new smallest cost node with MinDistance. (the function
ignores nodes marked as true).
We repeat the proces until there are no nodes left. 

Modules used:
-networkx -> graph manipulation and support for visualization
-matplotlib.pyplot -> plotting

# output

Left: initial graph
Right: Dijkstra graph that contains only the edges from parent array
