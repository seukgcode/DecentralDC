'''
构造数据共享交换行为范式：临时使用权共享、多方计算：
1、构造临时使用权共享行为范式
2、构造多方计算行为范式
注：共享交换行为包括上述两种行为，DB_share_name_list中的共享交换数据库要么参与使用权共享，要么参与多方计算法，要么同时参加。
本场景简单起见，DB_share_name_list中的数据库都有相应的使用权共享行为范式；DB_share_name_list的部分数据库设置多方计算行为范式。
'''

import random
import pickle

# 加载参与者相关信息
participant_info = 'scenario 01\\01 participant_info.pkl'
with open(participant_info, 'rb') as file_obj:
    participant_info_dic = pickle.load(file_obj)
ParticipantNum = participant_info_dic[0]        # 参与者数量
DB_num_list = participant_info_dic[1]           # 各参与方具有的数据库数量
DB_sharing_num_list = participant_info_dic[2]   # 参与方各自参与共享交换的数据库数量
DB_share_name_list = participant_info_dic[3]    # 参与方各自参与共享交换的数据库名称即ID
ParticipantList = ['P' + str(x + 1) for x in range(ParticipantNum)]  # 各参与方名字


Bx_paradigm_info = []                       # 行为范式信息（使用权共享与多方计算）
Bx_share_num = sum(DB_sharing_num_list)     # 共享使用权行为的数量
Bx_paradigm_id = 0                          # 共定义x种数据行为范式，ID为0-(x-1)
# 定义两种类型的ID
SHARE_TYPE_FLAG = 0
MULTICOMPUTE_TYPE_FLAG = 1

# 生成数据使用权临时共享行为范式
for i in range(ParticipantNum):
    for db in DB_share_name_list[i]:
        bx_share = []
        bx_share.append(Bx_paradigm_id)
        Bx_paradigm_id += 1
        bx_share.append(SHARE_TYPE_FLAG)
        bx_share.append('P'+str(i+1))
        bx_share.append(db)
        candidates = ParticipantList[:]
        candidates.remove(ParticipantList[i])
        permit_list = random.sample(candidates, random.randint(1, ParticipantNum - 1))  # 生成可以访问当前db的参与方列表
        bx_share.append(sorted(permit_list))
        Bx_paradigm_info.append(bx_share)

# 生成多方计算行为范式
Bx_multiCompute_num = round(Bx_share_num * 0.6)  # 定义多方计算行为的数量
for i in range(Bx_multiCompute_num):
    bx_mc = []
    bx_mc.append(Bx_paradigm_id)
    Bx_paradigm_id += 1
    bx_mc.append(MULTICOMPUTE_TYPE_FLAG)
    members = []  # 多方计算参与方
    members_index = sorted(random.sample(range(0, ParticipantNum), random.randint(2, ParticipantNum)))
    for index in members_index:
        members.append('P'+str(index+1))
    members_db = []  # 多方计算参与方数据库
    for index in members_index:
        members_db.append(random.choice(DB_share_name_list[index]))
    bx_mc.append(members)
    bx_mc.append(members_db)
    bx_mc.append(members)
    if bx_mc not in Bx_paradigm_info:
        Bx_paradigm_info.append(bx_mc)

# 写入txt文件，方便查看
filename = 'scenario 01\\02 bx_paradigm_info.txt'
with open(filename, 'w') as file_obj:
    for each in Bx_paradigm_info:
        for i in range(len(each)):
            file_obj.write(str(each[i]))
            if i == len(each) - 1:
                file_obj.write('\n')
            else:
                file_obj.write(' ')

# 写入pkl文件，方便存储与后续分析
filename_pkl = 'scenario 01\\02 bx_paradigm_info.pkl'
with open(filename_pkl, 'wb') as file_obj:
    pickle.dump(Bx_paradigm_info, file_obj)
