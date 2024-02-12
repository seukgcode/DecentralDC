'''
根据求得的行为范式权重，结合原始数据集中的数据量字段，量化参与共享交换的数据表贡献度；
'''
import pickle
import xlsxwriter as xw

def dic_sort_by_value(a_dict):      # 字典按值Value进行排序
    a_sort_list = sorted(a_dict.items(), key=lambda x : x[1], reverse=True)
    a_sort_dict = {}
    for n, s in a_sort_list:
        a_sort_dict[n] = s
    return a_sort_dict

# 读入原始数据集，对数据集后1/5部分进行贡献度评估测试
bx_seq_dataset_pkl = 'scenario 01\\04 bx_seq_dataset.pkl'
with open(bx_seq_dataset_pkl, 'rb') as file_obj:
    bx_seq_dataset = pickle.load(file_obj)

# 读入行为范式信息
bx_paradigm_info_pkl = 'scenario 01\\02 bx_paradigm_info.pkl'
with open(bx_paradigm_info_pkl, 'rb') as file_obj:
    bx_paradigm_info = pickle.load(file_obj)

# 读入行为范式权重
bx_paradigm_weight_pkl = 'scenario 01\\06 bx_paradigm_weight.pkl'
with open(bx_paradigm_weight_pkl, 'rb') as file_obj:
    bx_paradigm_weight = pickle.load(file_obj)

assess_dataset = bx_seq_dataset[int(0.8*len(bx_seq_dataset)):]
db_Contrib_dict = {}      # 存储各个数据库贡献度结果，并按贡献度降序排列
sum_dbc = 0               # 贡献度总和，归一化使用

for bx in assess_dataset:
    bx_paradigm_id = bx[3]
    if bx_paradigm_info[bx_paradigm_id][1] == 0:
        # 数据使用权共享行为
        sdb = bx_paradigm_info[bx_paradigm_id][3]
        db_Contrib_dict[sdb] = db_Contrib_dict.get(sdb, 0) + bx_paradigm_weight[bx_paradigm_id] * bx[-1][0]
        sum_dbc += bx_paradigm_weight[bx_paradigm_id] * bx[-1][0]
    else:
        # 多方计算行为
        for i in range(len(bx_paradigm_info[bx_paradigm_id][3])):
            sdb = bx_paradigm_info[bx_paradigm_id][3][i]
            db_Contrib_dict[sdb] = db_Contrib_dict.get(sdb, 0) + bx_paradigm_weight[bx_paradigm_id] * bx[-1][i]
            sum_dbc += bx_paradigm_weight[bx_paradigm_id] * bx[-1][i]

for bx_paradigm_id in db_Contrib_dict:
    db_Contrib_dict[bx_paradigm_id] = round(db_Contrib_dict[bx_paradigm_id] / sum_dbc, 5) * 100

db_Contrib_dict = dic_sort_by_value(db_Contrib_dict)
# print(db_Contrib_dict)

# 写入实验结果到Excel表格中，写3列数据即可
xlsx_file = 'scenario 01\\result-scale.xlsx'
workbook = xw.Workbook(xlsx_file)
worksheet1 = workbook.add_worksheet("sheet1")
worksheet1.activate()
title = ['序号', '数据库表', '贡献度（%）']
worksheet1.write_row('A1', title)
worksheet1.write_column('A2', [x+1 for x in range(len(db_Contrib_dict))])
worksheet1.write_column('B2', list(db_Contrib_dict.keys()))
worksheet1.write_column('C2', list(db_Contrib_dict.values()))
workbook.close()

