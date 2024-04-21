import numpy as np
from icecream import ic

# the anomaly detection method from paper FluxInfer
def fluxInfer(kpi, segments):
    if len(segments) < 2:
        return False
    last_seg = kpi[segments[-1][0]:segments[-1][1]+1]
    last_last_seg = kpi[segments[-2][0]:segments[-2][1]+1]
    # print(last_seg)
    # print(last_last_seg)
    last_last_mean, last_last_std = np.mean(last_last_seg), np.std(last_last_seg)
    if last_last_std == 0:
        return False
    last_z_score = (last_seg - last_last_mean) / last_last_std
    mean_z_score = np.mean(last_z_score)
    if np.abs(mean_z_score) > 3 * last_last_std:
        return True
    return False