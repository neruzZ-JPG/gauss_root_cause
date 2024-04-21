import numpy as np

def three_sigma(kpi, segments):
    avg = np.mean(kpi)
    std = np.std(kpi)
    threshold_up = avg + 3*std
    threshold_down = avg -3*std
    last_seg = kpi[segments[-1][0]:segments[-1][1]+1]
    last_mean = np.mean(last_seg)
    if last_mean < threshold_down or last_mean > threshold_up:
        return True
    return False
    