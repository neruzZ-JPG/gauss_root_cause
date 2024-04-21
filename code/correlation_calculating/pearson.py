import numpy as np

def pearson_correlation(x, y):

    x = np.array(x)
    y = np.array(y)

    # 计算相关系数
    correlation_coefficient = np.corrcoef(x, y)[0, 1]

    return correlation_coefficient