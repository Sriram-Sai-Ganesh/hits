import networkx as nx
import GraphUtils

# display scores as a table:
def displayTable(pairs, type=''):
    print(f'Node\t│ {type} Score')
    print('\n'.join([f'{x}\t│ {y:.3e}' for x,y in pairs]))

# display HITS hub and auth scores :
def displayScores(auth, hubs):
    print(f'HITS Scores:')
    print("\nTop 10 Authority Scores\n")
    displayTable(auth_sorted[:10], 'Authority')
    print("\nTop 10 Hub Scores\n")
    displayTable(hub_sorted[:10], 'Hub')

# graph = GraphUtils.importGraph('data/Cit-HepTh.txt')
graph = GraphUtils.importGraph()
GraphUtils.save_graph(graph)
GraphUtils.drawGraph(graph)

authority_scores, hub_scores = nx.hits(graph)
auth_sorted = sorted(authority_scores.items(), key=lambda x:x[1], reverse=True)
hub_sorted = sorted(authority_scores.items(), key=lambda x:x[1], reverse=True)

displayScores(auth_sorted, hub_sorted)
