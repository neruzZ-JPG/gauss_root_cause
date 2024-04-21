from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
import numpy as np
import random

# the data smoothing method from paper FluxInfer

'''
input: kpi, values of ONE kpi
output: smoothed_kpi, smoothed value of kpi
        segments, kpi splited
'''
def data_smoothing_from_paper(kpi):
    smoothed_kpi = kpi
    while True:
        # cluster into 2 clusters
        gmm = GaussianMixture(n_components=2, covariance_type='full', random_state=0)
        gmm.fit(np.array(smoothed_kpi).reshape(-1, 1))
        labels = gmm.predict(np.array(smoothed_kpi).reshape(-1, 1))
        # split into segments
        segments = get_segs(smoothed_kpi, labels)
        if len(segments) <= 2:
            return smoothed_kpi, segments
        # smooth
        def seg_len(seg):
            return seg[1] - seg[0] + 1
        for j in range(0, len(segments)-2):
            if seg_len(segments[j]) < seg_len(segments[j+1]):
                random_sample = smoothed_kpi[random.randint(segments[j+1][0], segments[j+1][1])]
                for k in range(segments[j][0], segments[j][1]+1):
                    smoothed_kpi[k] = random_sample
        return smoothed_kpi, segments
'''
input: kpi, labels
output: segments, aggregation of kpi based on labels 
        every segment is a list of [start, end, label]
'''
def get_segs(kpi, labels):
    # print(kpi)
    # print(labels)
    segments = []
    length = len(kpi)
    cur_seg = [0, 0, labels[0]]
    cur_label = labels[0]
    for i in range(1, length):
        if labels[i] == cur_label:
            continue
        else:
            cur_seg[1] = i-1
            segments.append(cur_seg)
            cur_seg = [i, i, labels[i]]
            cur_label = labels[i]
    cur_seg[1] = length-1
    segments.append(cur_seg)
    # print(segments)
    return segments


def data_smoothing_from_paper_test():
    # 生成模拟数据（两个聚类）
    X, y_true = make_blobs(n_samples=300, n_features=1, centers=2, cluster_std=1.0, random_state=0)
    plt.plot(range(0, len(X)), X)
    plt.show()
    X, segments = data_smoothing_from_paper(X)
    plt.plot(range(0, len(X)), X)
    plt.show()
#data_smoothing_from_paper_test()