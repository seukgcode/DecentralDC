'''
通过02中的行为范式设计协同业务场景流程，本课题对不同协同业务数据行为流程的要求：
1、任一bs不是其他bs的前缀
2、任一bs不包含在其他bs中
3、任一bs内不包含相同的bx
'''

import random
import pickle

def isSubSeq(seq1, seq2):       # 判断seq1是否是seq2的子序列（此处的子序列与序列模式的定义无关），seq1与seq2均为列表，即形如[2,3,5,6]
    if len(seq2) < len(seq1):
        return False
    if seq1 == seq2:
        return True

    if seq1[0] not in seq2:
        return False
    pre_pos = seq2.index(seq1[0])

    for i in range(1, len(seq1)):
        if seq1[i] not in seq2:
            return False
        if seq2.index(seq1[i]) < pre_pos:
            return False
        pre_pos = seq2.index(seq1[i])
    return True

def isSubBS(bs, bs_bx_seq):     # 判断bs是否是业务序列集中某个已有序列的子序列
    if len(bs_bx_seq) == 0:
        return False
    for exist_bs in bs_bx_seq:
        # 对于每一个exist_bs，判断bs是否是其子序列
        if isSubSeq(bs, exist_bs):
            return True
    return False

# 读取数据行为范式信息
filename_pkl = 'scenario 01\\02 bx_paradigm_info.pkl'
with open(filename_pkl, 'rb') as file_obj:
    bx_paradigm_info = pickle.load(file_obj)
bx_paradigm_num = len(bx_paradigm_info)       # 行为范式总数量

# 设计协同业务场景的数据行为范式流程，包含全部行为范式，不同业务场景行为序列不存在前缀关系
bs_num = 10  # 业务场景个数，业务场景要包含所有行为
bx_num_min_per_bs = 2
bx_num_max_per_bs = 5
bs_bx_seq = []  # 业务场景数据行为序列
bx_candidates = list(range(bx_paradigm_num))
while len(bs_bx_seq) != bs_num:
    bs = []     # 当前轮次要产生的bs，即bx序列
    bs_length = random.randint(bx_num_min_per_bs, bx_num_max_per_bs)     # 设定bs长度
    for j in range(bs_length):      # 逐位产生当前bs的交易行为
        if len(bx_candidates) >= 1:
            cur_bx = random.choice(bx_candidates)
            bs.append(cur_bx)
            bx_candidates.remove(cur_bx)
        else:
            while True:
                cur_bx = random.choice(range(bx_paradigm_num))
                if cur_bx not in bs:
                    bs.append(cur_bx)
                    break
    if not isSubBS(bs, bs_bx_seq):         # 判断当前bs是否为已有业务的子序列，若不是则作为新bs加入bs列表即bs_tx_seq
        bs_bx_seq.append(bs)


# 写入txt文件，方便查看
filename = 'scenario 01\\03 bs.txt'
with open(filename, 'w') as file_obj:
    for each in bs_bx_seq:
        for i in range(len(each)):
            file_obj.write(str(each[i]))
            if i == len(each) - 1:
                file_obj.write('\n')
            else:
                file_obj.write(' ')

# 写入pkl文件，方便存储与后续分析
filename_pkl = 'scenario 01\\03 bs.pkl'
with open(filename_pkl, 'wb') as file_obj:
    pickle.dump(bs_bx_seq, file_obj)

