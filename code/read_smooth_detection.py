import logging
import json
from data_smoothing.data_smoothing import data_smoothing
from anomaly_detection.anomaly_detection import anomaly_detection
import logging
import pandas as pd

def read_data(file):
    df = pd.read_csv(file)
    df = df.drop(columns="time")
    data = {}
    for column in df.columns:
    # 获取列名作为键
        key = column  
    # 获取该列的所有值
        values = df[column].tolist()
    # 将键值对添加到结果字典中
        data[key] = values
    return data

if __name__ == "__main__":

    config_file = 'config.json'
    with open(config_file, 'r', encoding='utf-8') as file:
        config = json.load(file)
    smooth_method = config["smooth_method"]
    anomoly_detection_method = config["anomaly_detection_method"]
    data_dir = config["data_dir"]
    data_file = config["data_file"]
    cache_dir = config["cache_dir"]
    
    # data reading
    with open(f'{data_dir}/{data_file}', 'r', encoding='utf-8') as f:
        data_infos = json.load(f)
    for data_info in data_infos:
        id = data_info['id']
        datas = read_data(f'{data_dir}/csv/{data_info["metrics"]}')
        anomalies = {}
        for key in datas.keys():
            kpi = datas[key]
            smoothed_kpi, segments = data_smoothing(kpi, smooth_method)
            if anomaly_detection(smoothed_kpi, segments, anomoly_detection_method):
                anomalies[key] = smoothed_kpi
        # 存异常文件
        with open(f'{cache_dir}/anomalies_{id}.json', 'w', encoding='utf-8') as f:
            json.dump(anomalies, f, ensure_ascii=False, indent=4)
    logging.info("step1 done")