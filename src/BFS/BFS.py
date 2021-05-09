#!/usr/bin/python3
# Copyright 2021 Stanciu Vlad

import networkx as nx
import matplotlib.pyplot as plt

def ReadGraph():
    G = nx.DiGraph()
    f = open("input.txt", "r")
    nodes = int(f.readline())

    # add edges to graph
    for i in range(nodes):
        line = list(map(int, (f.readline().split())))
        for j in range(nodes):
            if line[j] > 0:
                G.add_edge(i, j, length = line[j])

    for i in range(nodes):
        G.nodes[i]['distance'] = -1
    
    start = int(f.readline())

    return (G, start)

def DrawGraph(G, color_map):
    node_labels = nx.get_node_attributes(G, 'distance')
    plt.figure(num="BFS", figsize=(11, 7))

    # set fixed position of nodes
    # this is very important as we need the initial graph and BFS graph
    # to look identical
    # we also need the position for weight labels
    pos = nx.spring_layout(G)

    edge_labels = dict([((u,v,), d['length']) for u, v, d in G.edges(data = True)])

    # plot initial graph
    plt.subplot(121)
    plt.title("Initial graph")
    nx.draw(G, pos, node_color=color_map, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=11)
    
    # plot BFS graph
    plt.subplot(122)
    plt.title("Distance graph")
    nx.draw(G, pos, node_color=color_map, with_labels=True, labels=node_labels)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=11)
    
    plt.show()

def BFS(G, start):
    queue = []
    queue.append(start)
    G.nodes[start]['distance'] = 0
    
    # color map is used in draw function to set node colors
    color_map = []
    for _ in range(len(G.nodes)):
        color_map.append('blue')
    color_map[start] = 'green'

    while len(queue) > 0:
        front = queue.pop(0)
        print(front)
        ng = G.adj[front]
        for i in ng:
            # check if node was visited before
            if G.nodes[i]['distance'] == -1:
                queue.append(i)
                # mark node as visited
                G.nodes[i]['distance'] = G.nodes[front]['distance'] + 1
                if G.nodes[i]['distance'] % 2 == 0:
                    color_map[i] = 'red'
    return color_map


if __name__ == "__main__":
    (G, start) = ReadGraph()
    color_map = BFS(G, start)
    print(color_map)
    DrawGraph(G, color_map)
