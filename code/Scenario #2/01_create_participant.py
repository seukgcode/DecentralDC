'''
设置场景中的参与方情况
1、设置参与方个数及具有的数据库数目
2、设置每个参与方的参与共享交换的数据库数目，并随机设置相应的共享数据库形成列表

与normal区别：
1、参与方各自参与共享交换的数据库数量：random.uniform(0.2, 0.8)
'''

import random
import pickle

ParticipantNum = 50  # 参与方个数
ParticipantList = ['P' + str(x + 1) for x in range(ParticipantNum)]  # 各参与方名字
DB_num_list = [random.randint(3, 11) for x in range(ParticipantNum)]    # 各参与方具有的数据库数量
DB_sharing_num_list = [round(x * random.uniform(0.2, 0.8)) for x in DB_num_list]  # 参与方各自参与共享交换的数据库数量
DB_share_name_list = []  # 参与方各自参与共享交换的数据库名称即ID
for i in range(len(DB_num_list)):
    owner = ParticipantList[i]
    chosen_db = sorted(random.sample(range(DB_num_list[i]), DB_sharing_num_list[i]))
    cur_share_list = []
    for each in chosen_db:
        cur_share_list.append(owner + '-db-' + str(each + 1))
    DB_share_name_list.append(cur_share_list)

# 将数据存储到字典中
Dic = dict()
Dic[0] = ParticipantNum
Dic[1] = DB_num_list
Dic[2] = DB_sharing_num_list
Dic[3] = DB_share_name_list

# print(Dic[1])
# print(Dic[2])
# print(sum(Dic[2]))

# 写入txt文件，方便查看
filename = 'scenario 01\\01 participant_info.txt'
with open(filename, 'w') as file_obj:
    for each in DB_share_name_list:
        for i in range(len(each)):
            file_obj.write(str(each[i]))
            if i == len(each) - 1:
                file_obj.write('\n')
            else:
                file_obj.write(' ')

# 写入pkl文件，方便存储与后续分析
filename_pkl = 'scenario 01\\01 participant_info.pkl'
with open(filename_pkl, 'wb') as file_obj:
    pickle.dump(Dic, file_obj)
