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

def DrawGraph(G):
    pass


def MinDistance(G, dist, sptSet):
    min = sys.maxsize
    for node in range(len(G.nodes)):
         if dist[node] < min and sptSet[node] == False:
             min = dist[node]
             min_index = node
    return min_index

def Dijkstra(G, start):
    dist = []
    sptSet = []
    nodes = len(G.nodes)
    

    for i in range(nodes):
        dist.append(sys.maxsize)
        sptSet.append(False)
    dist[start] = 0

    for i in range(nodes - 1):
        u = MinDistance(G, dist, sptSet)
        sptSet[u] = True
        for node in range(nodes):
            if (u, node) in G.edges():
                if G.edges[u][node]["length"] > 0 and sptSet[node] == False and dist[node] > dist[u] + G.edges[u][node]["length"]:
                    dist[node] = dist[u] + G.edges[u][node]["length"]
        
        print(dist)


if __name__ == "__main__":
    (G, start) = ReadGraph()
    Dijkstra(G, start)
    #DrawGraph(G, color_map)