# Copyright Podaru Andrei-Alexandru 2021

DFS visualization tool allows you to see the initial graph and the result of
the DFS traversal for a directed, connected graph given by the user in input
file.

The format for the input file is as follows:
n (number of edges) -> integer
n * n adjency matrix, with one line / row => n lines with n integers each,
		      where a(i, j) = 1 if there is an edge from node i to node j
		      and a(i, j) = 0 otherwise
      -> integer matrix
start_node (node from which you begin the traversal) -> integer
All graph edges have length 1.

DFS function is implemented recursively, using discovery times as visited array.
The result can be seen by the user in the form of another graph, in which nodes
have labels on them that show discovery and completion times in DFS (traversal).
Discovery time represents the point in which we have first visited the node
during the traversal, and completion time represents the point in which we have
visited all neighbors of the given node. Times are represented in the form
discovery_time/completion_time, with time indexed from 0 to 2 * n - 1.

Modules used:
-networkx -> graph manipulation and support for visualization
-matplotlib.pyplot -> plotting
