'''
对于行为范式ID序列集，通过现有极大序列模式算法进行极大序列模式挖掘
可选择CM-SPADE进行一般频繁序列模式挖掘
'''

import pickle
from spmf import Spmf

def version_transform_txt(bx_paradigm_seq_set):
    filename = 'scenario 01\\05.2_inner bx_paradigm_seq_set_transform.txt'
    with open(filename, 'w') as file_obj:
        for bx_paradigm_seq in bx_paradigm_seq_set:
            for bx_itemset in bx_paradigm_seq:
                for i in range(len(bx_itemset)):
                    file_obj.write(str(bx_itemset[i])+' ')
                    if i == len(bx_itemset) - 1:
                        file_obj.write('-1 ')
            file_obj.write('-2\n')


# 获取待挖掘的序列数据集
bx_paradigm_seq_set_pkl = 'scenario 01\\05.1 bx_paradigm_seq_set.pkl'
with open(bx_paradigm_seq_set_pkl, 'rb') as file_obj:
    bx_paradigm_seq_set = pickle.load(file_obj)

# print(len(bx_paradigm_seq_set))
# print(bx_paradigm_seq_set[:10])

# 送入极大序列模式挖掘算法之前要进行格式转换
version_transform_txt(bx_paradigm_seq_set)

spmf = Spmf(algorithm_name="VMSP", input_filename="scenario 01\\05.2_inner bx_paradigm_seq_set_transform.txt",
            output_filename="scenario 01\\05.2 output_VMSP.txt", arguments=[0.017, "", "", False])

# spmf = Spmf(algorithm_name="CM-SPADE", input_filename="scenario 01\\05.2_inner bx_paradigm_seq_set_transform.txt",
            # output_filename="scenario 01\\05.2 output_VMSP.txt", arguments=[0.026, "", False])

spmf.run()
print(spmf.to_pandas_dataframe(pickle=True))

