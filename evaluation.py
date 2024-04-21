import json
from icecream import ic

def ac_k_one(scores, references, k):
    keys = scores.keys()
    count = 0
    for i in range(0, min(k, len(keys))):
        if list(keys)[i] in references:
            count += 1
    return count/min(k, len(references))

if __name__ == "__main__":
    config_file = 'config.json'
    with open(config_file, 'r', encoding='utf-8') as file:
        config = json.load(file)
    cache_dir = config["cache_dir"]
    data_dir = config["data_dir"]
    data_file = config["data_file"]
    cache_dir = config["cache_dir"]

    # data reading
    with open(f'{data_dir}/{data_file}', 'r', encoding='utf-8') as f:
        data_infos = json.load(f)
    ac_k_scores = {}
    for data_info in data_infos:
        id = data_info['id']
        with open(f'{cache_dir}/score_{id}.json', 'r', encoding='utf-8') as f:
            scores = json.load(f)
        # ac_k
        for k in range(1, 5):
            if k not in ac_k_scores.keys():
                ac_k_scores[k] = []
            ac_k_scores[k].append(ac_k_one(scores, data_info['root_causes'], k))
    
    sum_ac_k_score = 0
    for k in range(1, 5):
        ac_k_score = sum(ac_k_scores[k])/len(ac_k_scores[k])
        sum_ac_k_score += ac_k_score
        ic(ac_k_score)
        ic(sum_ac_k_score/k)
        # print(f'ac@{k} is {ac_k_score}')
        # print(f'avg@{k} is {sum_ac_k_score/k}')
    