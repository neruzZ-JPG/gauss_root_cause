from . import data_smoothing_from_paper
import matplotlib.pyplot as plt

def show_smooth_effect(kpi, smoothed_kpi):
    plt.plot(range(0, len(kpi)), kpi)
    plt.show()
    plt.plot(range(0, len(smoothed_kpi)), smoothed_kpi)
    plt.show()

def data_smoothing(kpi, method):
    algorythm = data_smoothing_from_paper.data_smoothing_from_paper
    if method == "from_paper":
        algorythm = data_smoothing_from_paper.data_smoothing_from_paper
    smoothed_kpi, segments = algorythm(kpi)    
    #show_smooth_effect(kpi, smoothed_kpi)
    return smoothed_kpi, segments