# interpretor
# Copyright 2021 Podaru Andrei-Alexandru


# modules import
import networkx as nx
import matplotlib.pyplot as plt


#read graph number of nodes, edges and start node for DFS
def ReadGraph():
    #directed graph with all edge lengths equal to 1
    G = nx.DiGraph()
    #input file
    fin = open("input.txt", "r")

    #number of nodes
    nodes = int(fin.readline())

    #add edges to graph
    for i in range(nodes):
        line = list(map(int, (fin.readline().split())))
        for j in range(nodes):
            if line[j] > 0:
                #there is an edge from node i to node j
                G.add_edge(i, j, length = line[j])

    #discovery and completion time attribute initialization
    for i in range(nodes):
        G.nodes[i]['time'] = [-1, -1]
    
    #start node for DFS
    start = int(fin.readline())

    #return the graph that was read from input file
    return (G, start)


#draw initial graph and graph after DFS traversal with discovery and
#completion times as labels for each node
def DrawGraph(G, color_map):
    #set node labels
    node_labels = nx.get_node_attributes(G, 'time')

    for i in range(len(G.nodes)):
        #convert node label from list format to dsc_time/cpl_time format
        times = node_labels[i]
        new_label = ""
        new_label += str(times[0])
        new_label += '/'
        new_label += str(times[1])
        node_labels[i] = new_label

    plt.figure(num="DFS", figsize=(12, 7))

    #set edge labels
    edge_labels = dict([((u,v,), d['length']) for u, v, d in G.edges(data = True)])

    #plot initial graph
    plt.subplot(121)
    plt.title("Initial graph")
    pos = nx.spring_layout(G)
    nx.draw(G, pos, node_color=color_map, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=11)
    
    #plot graph with traversal information
    plt.subplot(122)
    plt.title("Discovery and completion time - DFS")
    nx.draw(G, pos, node_color=color_map, with_labels=True, labels=node_labels)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=11)
    plt.show()


#global traversal time
time = 0

#DFS traversal with timestamps for nodes
def DFS(G, start):
    #set discovery time for current node
    global time
    G.nodes[start]['time'][0] = time
    time += 1

    #get neighbors for current node
    ng = G.adj[start]

    #traverse the neighbors if they weren't visited before
    for neighbor in ng:
        if G.nodes[neighbor]['time'][0] == -1:
            DFS(G, neighbor)
    
    #all neighbors were visited, we set the completion time
    G.nodes[start]['time'][1] = time
    time += 1


#main function
if __name__ == "__main__":
    #read input
    (G, start) = ReadGraph()

    #traverse graph
    DFS(G, start)

    #color all nodes in green
    color_map = []
    for i in range(len(G.nodes)):
        color_map.append('green')

    #draw initial graph and final graph (after traversal)
    #with timestamps
    DrawGraph(G, color_map)
