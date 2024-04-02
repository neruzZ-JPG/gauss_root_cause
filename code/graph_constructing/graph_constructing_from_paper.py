import networkx as nx
import math
import matplotlib.pyplot as plt


def WUDG(correlations, threshold):
    G = nx.DiGraph()
    for correlation in correlations:
        #print(type(correlation[2]))
        if math.isnan(correlation[2]):
            continue
        G.add_edge(correlation[0], correlation[1], weight=correlation[2])
        G.add_edge(correlation[1], correlation[0], weight=correlation[2])
    # nx.draw(G)
    # plt.show()
    return G
