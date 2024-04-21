import pandas as pd
from icecream import ic

def spearman_correlation(x, y):
    data = pd.DataFrame([x, y]).T
    # print(data)
    res = data.corr(method='spearman')
    # ic(res)
    return res[0][1]
