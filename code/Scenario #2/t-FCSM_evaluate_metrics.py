'''
主实验对比方法——2频繁连续子序列挖掘

1、在行为范式序列即上挖掘所有2频繁连续子序列集
2、构建行为范式依赖图并进行评价指标计算
'''

import pickle
from nltk import ngrams
import networkx as nx

def get_sup(patt, bx_paradigm_seq_set):
    itemset_list_size = len(bx_paradigm_seq_set)
    patt_count = 0
    for seq in bx_paradigm_seq_set:
        if len(seq) == 1:
            continue
        # 当前序列的所有长度为2的2频繁序列存进candidate_patt中
        candidate_patt = []
        grams_list = list(ngrams(seq, 2))
        for gram in grams_list:
            front = gram[0]
            post = gram[1]
            for x in front:
                for y in post:
                    if (x,y) not in candidate_patt:
                        candidate_patt.append((x,y))
        if patt in candidate_patt:
            patt_count += 1
    return patt_count / itemset_list_size

def evaluate(eval_DAG:nx.classes.digraph.DiGraph, bs_G:nx.classes.digraph.DiGraph):
    correct_edge_num = len(set(bs_G.edges) & set(eval_DAG.edges))
    precision = correct_edge_num / len(eval_DAG.edges)
    recall = correct_edge_num / len(bs_G.edges)
    F1 = (2 * precision * recall) / (precision + recall)
    print("precision: "+str(precision))
    print("recall: "+str(recall))
    print("F1: "+str(F1))

# 获取待挖掘的序列数据集
bx_paradigm_seq_set_pkl = 'scenario 01\\05.1 bx_paradigm_seq_set.pkl'
with open(bx_paradigm_seq_set_pkl, 'rb') as file_obj:
    bx_paradigm_seq_set = pickle.load(file_obj)

# 读取数据行为范式信息
filename_pkl = 'scenario 01\\02 bx_paradigm_info.pkl'
with open(filename_pkl, 'rb') as file_obj:
    bx_paradigm_info = pickle.load(file_obj)
bx_paradigm_num = len(bx_paradigm_info)

min_sup = 0.017
freq_2continuous_patt = []
for x in range(bx_paradigm_num):
    for y in range(x+1, bx_paradigm_num):
        patt = (x,y)
        re_patt = (y,x)

        sup = get_sup(patt, bx_paradigm_seq_set)
        re_sup = get_sup(re_patt, bx_paradigm_seq_set)

        if sup >= min_sup:
            freq_2continuous_patt.append(patt+(sup,))
        if re_sup >= min_sup:
            freq_2continuous_patt.append(re_patt+(re_sup,))

two_FCSM_G = nx.DiGraph()
two_FCSM_G.add_weighted_edges_from(freq_2continuous_patt)

# 读取业务场景数据交易行为序列，以创建原始、正确的有向图
filename_pkl = 'scenario 01\\03 bs.pkl'
with open(filename_pkl, 'rb') as file_obj:
    bs_info = pickle.load(file_obj)
bs_num = len(bs_info)

bs_G = nx.DiGraph()       # 创建原始、正确的有向图
for bs in bs_info:
    two_gram_list = list(ngrams(bs, 2))
    bs_G.add_edges_from(two_gram_list)

# 计算精确度、召回率、F1值
evaluate(two_FCSM_G, bs_G)

