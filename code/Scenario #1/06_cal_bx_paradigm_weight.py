'''
主实验部分
根据极大序列模式构建行为范式依赖图，并根据度中心性计算各行为范式重要度权重
'''

import pickle
import networkx as nx
from nltk import ngrams

def cal_bx_weight(weight_DAG:nx.classes.digraph.DiGraph, weight_type):   # 计算有向图节点的重要度即交易行为的权重
    # 可能会有不连通子图的情况
    # 有向图对应无向图的连通分支数：u_g = d.to_undirected(); len(list(nx.connected_components(u_g)，u_g为无向图
    bx_weight_dict = {}

    if weight_type == 1:        # 连通分支数对其无影响
        # 用度中心性评价，nx包中自带的degree_centrality(g)算法基于无向图的ki/(n-1)公式进行计算，未进行“归一化”
        # 转化成无向图方便计算
        sum_degree_centrality = 0
        u_g = weight_DAG.to_undirected()
        for node in u_g.nodes:
            bx_weight_dict[node] = 0
            for adj in u_g[node]:
                bx_weight_dict[node] += u_g[node][adj]['weight']
                sum_degree_centrality += u_g[node][adj]['weight']
        for node in bx_weight_dict:
            bx_weight_dict[node] /= sum_degree_centrality

    elif weight_type == 2:      # 连通分支数对其无影响
        # 用类PageRank评价
        bx_weight_dict = nx.pagerank(weight_DAG, alpha=0.9, max_iter=10000)

    elif weight_type == 3:      # 连通分支数对其无影响
        # 用特征向量中心性评价，可能不容易收敛
        bx_weight_dict = nx.eigenvector_centrality(weight_DAG, max_iter=10000, weight="weight")

    return bx_weight_dict

def dic_sort_by_value(a_dict):      # 字典按值Value进行排序
    a_sort_list = sorted(a_dict.items(), key=lambda x : x[1], reverse=True)
    a_sort_dict = {}
    for n, s in a_sort_list:
        a_sort_dict[n] = s
    return a_sort_dict

# 获取待挖掘的序列数据集基数，为了计算各极大序列模式的支持度（0-1之间）
bx_paradigm_seq_set_pkl = 'scenario 01\\05.1 bx_paradigm_seq_set.pkl'
with open(bx_paradigm_seq_set_pkl, 'rb') as file_obj:
    bx_paradigm_seq_set = pickle.load(file_obj)
bx_paradigm_seq_set_len = len(bx_paradigm_seq_set)

# 读取挖掘出的极大序列模式
MSP_pkl = 'scenario 01\\05.2 output_VMSP.pkl'
with open(MSP_pkl, 'rb') as file_obj:
    MSP_set = pickle.load(file_obj)

# print(MSP_set)
MSP_list = []       # 列表形式存储的极大序列模式
MSP_sup_list = []   # 对应的极大序列模式的支持度

for i in range(len(MSP_set['pattern'])):
    MSP = []
    for itemset_str in MSP_set['pattern'][i]:
        temp = itemset_str.split()
        MSP.append(temp)
    MSP_list.append(MSP)
    MSP_sup_list.append(round(MSP_set['sup'][i] / bx_paradigm_seq_set_len, 3))

# print(MSP_list)
# print(MSP_sup_list)

# 根据行为范式极大序列模式与支持度构建行为范式依赖图
bx_Dependency_Graph = nx.DiGraph()
for i in range(len(MSP_list)):
    msp = MSP_list[i]
    two_gram_list = list(ngrams(msp, 2))
    # print(two_gram_list)
    for two_gram in two_gram_list:
        x_itemset = two_gram[0]
        y_itemset = two_gram[1]
        for x in x_itemset:
            for y in y_itemset:
                if (int(x), int(y)) not in bx_Dependency_Graph.edges:
                    bx_Dependency_Graph.add_edge(int(x), int(y), weight=MSP_sup_list[i])
                else:
                    bx_Dependency_Graph[int(x)][int(y)]['weight'] += MSP_sup_list[i]

# 利用行为依赖图进行节点重要性评估，得到各行为范式权重
weight_type = 1     # 表示用度中心性进行评估
bx_weight = cal_bx_weight(bx_Dependency_Graph, weight_type)       # 返回字典类型，key=行为ID，value=行为重要度权重
bx_weight = dic_sort_by_value(bx_weight)
# print(bx_weight)

filename_pkl = 'scenario 01\\06 bx_paradigm_weight.pkl'
with open(filename_pkl, 'wb') as file_obj:
    pickle.dump(bx_weight, file_obj)
