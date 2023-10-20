import networkx as nx
import matplotlib.pyplot as plt

def import_graph(filename = './data/graph.txt', isNetworkXGraph=True):
    result = nx.DiGraph() if isNetworkXGraph else dict()
    with open(filename) as file:
        for line in file:
            nodes=line.strip().split()
            if len(nodes) < 1:
                    continue
            print(f'{nodes[0]} is adjacent to all {nodes[1:]}')
            start=nodes[0]
            if isNetworkXGraph:
                for neighbor in nodes[1:]:
                    result.add_edge(start, neighbor)
            else:
                result[start]=nodes[1:]
    return result

graph = import_graph()
print(f'\nLoaded a graph:\n{graph}')
nx.draw(graph, with_labels=True)
plt.show()

authority_scores, hub_scores = nx.hits(graph)
print("\nAuthority Scores:")
print('\n'.join(list(map(str, authority_scores.items()))))
print("Hub Scores:")
print('\n'.join(list(map(str, hub_scores.items()))))
