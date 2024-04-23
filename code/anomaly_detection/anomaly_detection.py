from . import fluxInfer
from . import grubbs
from . import three_sigma
from . import outlier

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
    return algorythm(kpi, segments)
