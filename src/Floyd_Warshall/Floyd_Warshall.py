#!/usr/bin/python3
# Copyright 2021 Popescu Silviu


# networkx - graph manipulation
# matplotlib.pyplot - graph plotting
import sys
import networkx as nx
import matplotlib.pyplot as plt

def ReadGraph():
    # directed graph
    G = nx.DiGraph()
    f = open("input.txt", "r")

    # number of nodes
    nodes = int(f.readline())

    # add edges & length to graph
    for i in range(nodes):
        line = list(map(int, (f.readline().split())))
        for j in range(nodes):
            # verifies if there is an edge from node i to j
            if line[j] > 0:
                G.add_edge(i, j, length = line[j])


    return G

# plots initial graph
def DrawGraph(G, color_map):
    # set nodes labels
    node_labels = nx.get_node_attributes(G, 'length')
    plt.figure(num = "Floyd Warshall", figsize = (11, 7))


    pos = nx.spring_layout(G)

    # set edge labels
    edge_labels = dict([((u,v,), d['length']) for u, v, d in G.edges(data = True)])

    # plot initial graph
    plt.plot()
    plt.title("Initial graph")
    nx.draw(G, pos, node_color = color_map, with_labels = True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=11)

    plt.show()

# implementation of Floyd Warshall algorithm
# INF <-> there is no path between two nodes 
INF = sys.maxsize
def FW(G):

    w = len(G.nodes)
    dist = [[0 for x in range(w)] for y in range(w)] 

    color_map = []

    for i in range(len(G.nodes)):
        color_map.append('coral')

    vertices = len(G.nodes)

    # create initial minimum-distrance matrix = dist
    for u in range(vertices):
        for v in range(vertices):
            if u == v:
                dist[u][v] = INF
            elif G.edges[u][v]["length"] <= 0:
                dist[u][v] = INF
            else:
                dist[u][v] = G.edges[u][v]["length"]

    # update the matrix with the minimum distance between each pair of nodes
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return (dist, color_map)


if __name__ == "__main__":
    G = ReadGraph()
    tup = FW(G)
    # print the distance matrix
    for i in tup[0]:
        print(i)

    # plot initial graph
    DrawGraph(G, tup[1])
