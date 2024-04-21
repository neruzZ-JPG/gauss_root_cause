
from . import graph_constructing_from_paper 

def graph_constructing(correlations, threshold, method):
    algorythm = "WUDG"
    if method == "WUDG":
        algorythm = graph_constructing_from_paper.WUDG
    return algorythm(correlations, threshold)
