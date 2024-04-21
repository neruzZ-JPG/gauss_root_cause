# 相关系数存下来
import json
from correlation_calculating.correlation_calculating import correlation_calculating

if __name__ == "__main__":
    config_file = 'config.json'
    with open(config_file, 'r', encoding='utf-8') as file:
        config = json.load(file)
    correlation_method = config['correlation_method']
    data_dir = config["data_dir"]
    data_file = config["data_file"]
    cache_dir = config["cache_dir"]
    
    # data reading
    with open(f'{data_dir}/{data_file}', 'r', encoding='utf-8') as f:
        data_infos = json.load(f)
    for data_info in data_infos:
        id = data_info['id']
        with open(f'{cache_dir}/anomalies_{id}.json', 'r', encoding='utf-8') as f:
            anomolies = json.load(f)
        correlations = correlation_calculating(anomolies, correlation_method)
        with open(f'{cache_dir}/correlations_{id}.json', 'w', encoding='utf-8') as f:
            json.dump(correlations, f, ensure_ascii=False, indent=4)