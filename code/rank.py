import json
import networkx as nx
from node_ranking.node_ranking import node_ranking

def json2graph(graph_data):
    G = nx.DiGraph()
    for node in graph_data['nodes']:
        G.add_node(node['id'])
    for edge in graph_data['edges']:
        G.add_edge(edge['source'], edge['target'], weight=edge['weight'])
    return G


if __name__ == "__main__":
    config_file = 'config.json'
    with open(config_file, 'r', encoding='utf-8') as file:
        config = json.load(file)
    method = config['ranking_method']
    data_dir = config["data_dir"]
    data_file = config["data_file"]
    cache_dir = config["cache_dir"]
    
    # data reading
    with open(f'{data_dir}/{data_file}', 'r', encoding='utf-8') as f:
        data_infos = json.load(f)
    for data_info in data_infos:
        id = data_info['id']
        with open(f'{cache_dir}/graph_{id}.json', 'r', encoding='utf-8') as f:
            graph_json = json.load(f)
        graph = json2graph(graph_json)
        rank_score = node_ranking(graph, method)
        rank_score = dict(sorted(rank_score.items(), key=lambda item: item[1], reverse=True))
        with open(f'{cache_dir}/score_{id}.json', 'w', encoding='utf-8') as f:
            json.dump(rank_score, f, ensure_ascii=False, indent=4)