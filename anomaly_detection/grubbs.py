import numpy as np
from scipy import stats


def grubbs(kpi, segments):
    mean = np.mean(kpi)
    std = np.std(kpi)
    if std == 0:
        return False
    last_seg = kpi[segments[-1][0]:segments[-1][1]+1]
    last_mean = np.mean(last_seg)

    n = len(segments)
    alpha = 0.05
    t_critical = stats.t.ppf(1-alpha/(2*n), n-2)
    g = ((n-1)/np.sqrt(n)) * np.sqrt(np.square(t_critical)/(n-2+np.square(t_critical)))                     
    grubbs_val = (last_mean - mean) / std         

    # 计算临界值
    t_critical = stats.t.ppf(1-alpha/(2*n), n-2)
    c = (n-1)/np.sqrt(n**2) * np.sqrt(np.square(t_critical)/(n-2+np.square(t_critical))) 
    if grubbs_val > c:
        return True
    return False