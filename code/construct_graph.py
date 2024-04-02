import json
from graph_constructing.graph_constructing import graph_constructing

def graph2json(G):
    nodes = [{'id': node} for node in G.nodes()]
    edges = [{'source': edge[0], 'target': edge[1], 'weight': edge[2]['weight']} for edge in G.edges(data=True)]
    graph_data = {'nodes': nodes, 'edges': edges}
    json_data = json.dumps(graph_data, indent=4)
    return json_data

if __name__ == "__main__":
    config_file = 'config.json'
    with open(config_file, 'r', encoding='utf-8') as file:
        config = json.load(file)
    cache_dir = config["cache_dir"]
    threshold = config["graph_threshold"]
    method = config['graph_constructing_method']
    data_dir = config["data_dir"]
    data_file = config["data_file"]
    cache_dir = config["cache_dir"]
    
    # data reading
    with open(f'{data_dir}/{data_file}', 'r', encoding='utf-8') as f:
        data_infos = json.load(f)
    for data_info in data_infos:
        id = data_info['id']
        with open(f'{cache_dir}/correlations_{id}.json', 'r', encoding='utf-8') as f:
            correlations = json.load(f)
        graph = graph_constructing(correlations, threshold, method)
        with open(f'{cache_dir}/graph_{id}.json', 'w', encoding='utf-8') as f:
            f.write(graph2json(graph))


