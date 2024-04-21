from . import fluxInfer
from . import grubbs
from . import three_sigma
from . import outlier

def pipe(kpi, segments):
    methods = [
        fluxInfer.fluxInfer,
        three_sigma.three_sigma,
        grubbs.grubbs,
        outlier.outlier
    ]
    for method in methods:
        if method(kpi, segments):
            return True
    return False

def anomaly_detection(kpi, segments, method):
    algorythm = fluxInfer.fluxInfer
    if method == 'fluxInfer':
        algorythm = fluxInfer.fluxInfer
    if method == 'three_sigma':
        algorythm = three_sigma.three_sigma
    if method == 'grubbs':
        algorythm = grubbs.grubbs
    if method == 'outlier':
        algorythm = outlier.outlier
    if method == 'all':
        algorythm = pipe      
    return algorythm(kpi, segments)
