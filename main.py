import os
import json
import re
from unicodedata import name
from matplotlib import pyplot as plt
# data_folder = os.path.join(os.path.expanduser("~"), "Data", "twitter")
# friends_filename = os.path.join(data_folder, "python_friends.json")
mockdata_name = "./mock.json"
data = []
with open(mockdata_name) as f:
    data = json.load(f)

def get_relevant(data):
    relevants = []
    # relevants.append((0,{"record_id": 0, "rel_info":[]}))
    for d in data:
        record_id = d['id']
        # relevants.append({"record_id": record_id, "rel_info":[]})
        rel_data = {"record_id": record_id, "rel_info":[], "weight":1}
        for rel in data:
            if d['id'] == rel['id'] : continue
            fault_type = rel['fault_type']
            rel_id = rel['id']
            server_product_id = rel['server_product_id']
            fw_bios = rel['fw_bios']
            idc = rel['idc']
            if d['fault_type'] == fault_type:
                # print("relevants -- record_id", relevants.get(record_id))
                info = {"rel_id": rel_id, "fault_id": fault_type}
                rel_data["rel_info"].append(info)
            if d['server_product_id'] == server_product_id:
                info  = {"rel_id": rel_id, "server_product_id": server_product_id}
                rel_data["rel_info"].append(info)
            if d['fw_bios'] == fw_bios:
                info =  {"rel_id": rel_id, "fw_bios": fw_bios}
                rel_data["rel_info"].append(info)
            if d['idc'] == idc:
                info = {"rel_id": rel_id, "idc": idc}
                rel_data["rel_info"].append(info)
        rel_data["weight"] += len(rel_data["rel_info"])
        relevants.append((record_id, rel_data))

    return relevants

def gen_graph(data:dict):
    import networkx as nx
    G = nx.DiGraph()
    G.add_nodes_from(data)
    print(list(G.nodes))
    # gen graph
    for node in data:
        for rel in node[1]['rel_info']:
            # rel_node = data[rel['rel_id']]
            edge_name = list(rel.keys())[1]
            G.add_edge(node[0], rel['rel_id'], weight=node[1]['weight'], name=edge_name)
            # print("main: ", node[0],"\nrel:", rel_node[0])
    pos = nx.spring_layout(G, iterations=20)
    nx.draw(G, pos, alpha=0.1, edge_color='b', with_labels=True)
    edge_attr = nx.get_edge_attributes(G, 'name')
    nx.draw_networkx_edge_labels(G, pos, edge_attr)
    plt.show()

rel = get_relevant(data["list"])
gen_graph(rel)
# print(rel)