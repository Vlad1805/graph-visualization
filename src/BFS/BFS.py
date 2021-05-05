import networkx as nx
import matplotlib.pyplot as plt

def ReadGraph():
    G = nx.DiGraph()
    f = open("input.txt", "r")
    nodes = int(f.readline())
    for i in range(nodes):
        line = list(map(int, (f.readline().split())))
        for j in range(nodes):
            if line[j] > 0:
                G.add_edge(i, j, length = line[j])

    for i in range(nodes):
        G.nodes[i]['degree'] = -1
    
    start = int(f.readline())

    return (G, start)

def DrawGraph(G, color_map):
    node_labels = nx.get_node_attributes(G, 'degree')
    plt.figure(num="BFS", figsize=(11, 7))
    plt.subplot(121)
    plt.title("Initial graph")
    pos = nx.spring_layout(G)
    nx.draw(G, pos, node_color=color_map, with_labels=True)
    edge_labels = dict([((u,v,), d['length']) for u, v, d in G.edges(data = True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=11)
    plt.subplot(122)
    plt.title("Degree graph")
    nx.draw(G, pos, node_color=color_map, with_labels=True, labels=node_labels)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=11)
    plt.show()

def BFS(G, start):
    queue = []
    queue.append(start)
    G.nodes[start]['degree'] = 0
    color_map = []
    color_map.append('green')
    while len(queue) > 0:
        front = queue.pop(0)
        print(front)
        ng = G.adj[front]
        for i in ng:
            if G.nodes[i]['degree'] == -1:
                queue.append(i)
                G.nodes[i]['degree'] = G.nodes[front]['degree'] + 1
                if G.nodes[i]['degree'] % 2 == 0:
                    color_map.append('red')
                else:
                    color_map.append('blue')
    return color_map


if __name__ == "__main__":
    (G, start) = ReadGraph()
    color_map = BFS(G, start)
    print(color_map)
    DrawGraph(G, color_map)
