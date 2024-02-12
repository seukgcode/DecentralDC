'''
根据挖掘到的极大序列模式计算 精确率、召回率与F1值
'''

import pickle
import networkx as nx
from nltk import ngrams

def evaluate(eval_DAG:nx.classes.digraph.DiGraph, bs_G:nx.classes.digraph.DiGraph):
    correct_edge_num = len(set(bs_G.edges) & set(eval_DAG.edges))
    precision = correct_edge_num / len(eval_DAG.edges)
    recall = correct_edge_num / len(bs_G.edges)
    F1 = (2 * precision * recall) / (precision + recall)
    print("precision: "+str(precision))
    print("recall: "+str(recall))
    print("F1: "+str(F1))

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

# 分别构建行为依赖图
# 读取业务场景数据交易行为序列，以创建原始、正确的有向图
filename_pkl = 'scenario 01\\03 bs.pkl'
with open(filename_pkl, 'rb') as file_obj:
    bs_info = pickle.load(file_obj)
bs_num = len(bs_info)

bs_G = nx.DiGraph()       # 创建原始、正确的有向图
for bs in bs_info:
    two_gram_list = list(ngrams(bs, 2))
    bs_G.add_edges_from(two_gram_list)


# 根据行为范式极大序列模式与支持度构建行为范式依赖图
MSP_Graph = nx.DiGraph()
for i in range(len(MSP_list)):
    msp = MSP_list[i]
    two_gram_list = list(ngrams(msp, 2))
    # print(two_gram_list)
    for two_gram in two_gram_list:
        x_itemset = two_gram[0]
        y_itemset = two_gram[1]
        for x in x_itemset:
            for y in y_itemset:
                if (int(x), int(y)) not in MSP_Graph.edges:
                    MSP_Graph.add_edge(int(x), int(y), weight = MSP_sup_list[i])
                else:
                    MSP_Graph[int(x)][int(y)]['weight'] += MSP_sup_list[i]

# 输出挖掘到的MSP的最大长度
max_length = 0
for each in MSP_set['pattern']:
    if len(each) > max_length:
        max_length = len(each)
print('max_length:', max_length)
# 计算精确度、召回率、F1值
evaluate(MSP_Graph, bs_G)
