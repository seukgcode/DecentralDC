'''
输入原始数据集，进行预处理，预处理包括两部分
1、通过两个划分间隔阈值进行划分
2、通过滑动窗口进行划分
'''

import pickle

def preprocess(bx_seq_raw, sliding_window_size, sliding_step):
    # 按划分间隔阈值进行划分，相同时间的行为组成一个项集（内部不分顺序，按字典序排列）
    bx_seq_itemset_list = []
    bx_list = []
    bx_list.append([bx_seq_raw[0][1]])
    partition_threshold = 5         # 划分间隔阈值
    for i in range(1, len(bx_seq_raw)):
        if int(bx_seq_raw[i][0]) - int(bx_seq_raw[i-1][0]) == 0:
            # 行为在相同时间发生，作为同一项集
            temp = bx_list.pop()
            temp.append(bx_seq_raw[i][1])
            bx_list.append(sorted(temp))
        elif int(bx_seq_raw[i][0]) - int(bx_seq_raw[i-1][0]) <= partition_threshold:
            bx_list.append([bx_seq_raw[i][1]])
        else:
            bx_seq_itemset_list.append(bx_list)
            bx_list = []
            bx_list.append([bx_seq_raw[i][1]])
    if len(bx_list) != 0:       # 将最后一个tx_list加入到tx_seq_itemset_list中
        bx_seq_itemset_list.append(bx_list)

    # 根据滑动窗口与滑动步长构造待挖掘的项集
    bx_paradigm_seq_set = []
    for eachList in bx_seq_itemset_list:
        if len(eachList) == 1:
            continue
        if len(eachList) <= sliding_window_size:
            bx_paradigm_seq_set.append(eachList)
        else:
            for left in range(0, len(eachList), sliding_step):
                right = left + sliding_window_size
                if right >= len(eachList):
                    if len(eachList[left:]) == 1:       # 剩的“尾巴”长度为1，加入到前一个末尾，不作为新的项集
                        bx_paradigm_seq_set[-1].extend(eachList[left:])
                    else:
                        bx_paradigm_seq_set.append(eachList[left:])
                    break
                else:
                    bx_paradigm_seq_set.append(eachList[left:right])
    return bx_paradigm_seq_set


bx_seq_dataset_pkl = 'scenario 01\\04 bx_seq_dataset.pkl'
with open(bx_seq_dataset_pkl, 'rb') as file_obj:
    bx_seq_dataset = pickle.load(file_obj)
bx_seq_raw = []         # 根据数据集提取（时间戳，行为范式ID）元组
for each in bx_seq_dataset:
    bx_seq_raw.append((each[2], each[3]))

# 行为序列数据集预处理
sliding_window_size = 8         # 作用：距离限制，距离太远认为没有关联；窗口较大时，序列变长不利于挖掘频繁模式
sliding_step = 8                # 滑动步长
bx_paradigm_seq_set = preprocess(bx_seq_raw, sliding_window_size, sliding_step)

# print(bx_paradigm_seq_set)
# [ [[0], [4], [1], [3], [2]], [[7], [8, 3], [7, 8], [9, 12], [6, 0]], [[3, 4], [1, 11], [3], [10, 2]],....,
# print(len(bx_paradigm_seq_set))     # 1407


filename_pkl = 'scenario 01\\05.1 bx_paradigm_seq_set.pkl'
with open(filename_pkl, 'wb') as file_obj:
    pickle.dump(bx_paradigm_seq_set, file_obj)
