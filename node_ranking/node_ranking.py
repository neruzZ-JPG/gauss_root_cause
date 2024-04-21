from . import fluxinfer
from . import pagerank

def node_ranking(graph, method):
    algorythm = pagerank.pagerank
    if method == "FluxInfer":
        algorythm = fluxinfer.fluxinfer_pagerank
    if method == "pagerank":
        algorythm = pagerank.pagerank
    return algorythm(graph)
    