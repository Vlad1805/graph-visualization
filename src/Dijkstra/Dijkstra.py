#!/bin/python3
# Copyright 2021 Stanciu Vlad

import networkx as nx
import matplotlib.pyplot as plt
import sys

def ReadGraph():
    G = nx.DiGraph()
    f = open("input.txt", "r")
    nodes = int(f.readline())

    for i in range(nodes):
        line = list(map(int, (f.readline().split())))
        for j in range(nodes):
            if line[j] > 0:
                G.add_edge(i, j, length=line[j])

    for i in range(nodes):
        G.nodes[i]['degree'] = -1
    
    start = int(f.readline())

    return (G, start)

def DrawGraph(G, D, start):
    #node_labels = nx.get_node_attributes(G, 'degree')
    plt.figure(num="Dijkstra", figsize=(12, 7))
    color_map = []
    for _ in range(len(G.nodes)):
        color_map.append('blue')
    color_map[start] = 'green'
    plt.subplot(121)
    plt.title("Initial graph")
    pos = nx.spring_layout(G)
    nx.draw(G, pos, node_color=color_map, with_labels=True)
    edge_labels = dict([((u,v,), d['length']) for u, v, d in G.edges(data = True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=11)
    
    plt.subplot(122)
    plt.title("Shortest path graph")
    nx.draw(D, pos, node_color=color_map, with_labels=True)
    edge_labels2 = dict([((u,v,), d['length']) for u, v, d in D.edges(data = True)])
    nx.draw_networkx_edge_labels(D, pos, edge_labels=edge_labels2, label_pos=0.3, font_size=11)
    plt.show()


def MinDistance(G, dist, sptSet):
    min = sys.maxsize
    min_index = -1
    for node in range(len(G.nodes)):
         if dist[node] < min and sptSet[node] == False:
             min = dist[node]
             min_index = node
    return min_index

def Dijkstra(G, start):
    dist = []
    sptSet = []
    parent = []
    nodes = len(G.nodes)
    

    for _ in range(nodes):
        dist.append(sys.maxsize)
        sptSet.append(False)
        parent.append(-1)
    dist[start] = 0

    for _ in range(nodes - 1):
        u = MinDistance(G, dist, sptSet)
        if u == -1:
            break
        sptSet[u] = True
        for node in range(nodes):
            if (u, node) in G.edges():
                if G[u][node]["length"] > 0 and sptSet[node] == False and dist[node] > dist[u] + G[u][node]["length"]:
                    dist[node] = dist[u] + G[u][node]["length"]
                    parent[node] = u

    print("Distance array:", end=" ")
    print(dist)
    print("Parent array:", end=" ")
    print(parent)

    D = nx.DiGraph()
    for node in range(nodes):
        D.add_node(node)
    for node in range(nodes):
        if parent[node] != -1:
            D.add_edge(parent[node], node, length=G[parent[node]][node]["length"])

    return D


if __name__ == "__main__":
    (G, start) = ReadGraph()
    D = Dijkstra(G, start)
    DrawGraph(G, D, start)