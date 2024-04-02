from . import pearson

'''
input:  kpis, dict
        method, str
output: list of [key1, key2, correlation_value]
'''
def correlation_calculating(kpis, method):
    algorythm = pearson.pearson_correlation
    if method == 'pearson':
        algorythm = pearson.pearson_correlation
    res = []
    keys = list(kpis.keys())
    # 遍历字典的键，进行两两配对
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            key1, key2 = keys[i], keys[j]
            correlation = algorythm(kpis[key1], kpis[key2])
            res.append([key1, key2, correlation])
    #print(res)
    return res
            

