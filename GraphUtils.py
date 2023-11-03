import networkx as nx
import matplotlib.pyplot as plt


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
    print(f'\nLoaded a graph:\n{graph}')
    return result

# draw a networkx graph:
def drawGraph(graph):
    nx.draw(graph, with_labels=True)
    plt.show()