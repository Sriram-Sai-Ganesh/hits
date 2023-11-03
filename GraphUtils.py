import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import pylab


# data in the file is a list of adjacency pairs forming a directed graph.
def importGraph(filename = './data/trivial.txt', isNetworkXGraph=True):
    result = nx.DiGraph() if isNetworkXGraph else dict()
    with open(filename) as file:
        for line in file:
            if line[0]=='#':
                continue
            fromNode, toNode = map(int, line.strip().split())
            # print(f'{nodes[0]} is adjacent to {nodes[1:]}')
            if isNetworkXGraph:
                # for neighbor in nodes[1:]:
                result.add_edge(fromNode, toNode)
            else:
                if fromNode in result:
                    result[fromNode].append(toNode)
                else:
                    result[fromNode]=[toNode]
    print(f'\nLoaded a graph:\n{result}')
    return result

# draw a networkx graph:
def drawGraph(graph):
    nx.draw(graph, with_labels=True)
    plt.show()


def save_graph(graph,file_name='out/graph.pdf'):
    #initialize fig
    plt.figure(num=None, figsize=(20, 20), dpi=8)
    plt.axis('off')
    fig = plt.figure(1)
    # pos = nx.spring_layout(graph)
    pos = nx.circular_layout(graph)
    nx.draw_networkx_nodes(graph,pos)
    nx.draw_networkx_edges(graph,pos)
    nx.draw_networkx_labels(graph,pos)

    cut = 1.2
    xmax = cut * max(xx for xx, _ in pos.values())
    ymax = cut * max(yy for _, yy in pos.values())
    plt.xlim(-xmax, xmax)
    plt.ylim(-ymax, ymax)

    plt.savefig(file_name,bbox_inches="tight")
    pylab.close()
    del fig