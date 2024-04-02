import networkx as nx

def pagerank(G):
    pagerank_scores = nx.pagerank(G ,max_iter=1000)
    return pagerank_scores