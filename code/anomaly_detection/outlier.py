import numpy as np

def outlier(kpi, segments):
    iqr = np.quantile(kpi,0.75) - np.quantile(kpi,0.25)
    quan_down = np.quantile(kpi,0.25)-1.5*iqr
    quan_up = np.quantile(kpi,0.75)+1.5*iqr
    last_seg = kpi[segments[-1][0]:segments[-1][1]+1]
    last_mean = np.mean(last_seg)
    if last_mean < quan_down or last_mean > quan_up:
        return True
    return False