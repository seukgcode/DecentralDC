'''
模拟协同业务并行执行，构造共享交换行为范式序列（区块链上记录的元数据序列），即本任务数据集
1、每个业务专门有一个线程进行循环执行
2、每隔一段随机时间，一定概率发生本次业务，确认发生此业务时，业务内行为之间间隔较短
'''

import pickle
import random
import threading

class myThread (threading.Thread):
    def __init__(self, thread_bs_id, name, clock_max):
        threading.Thread.__init__(self)
        self.thread_bs_id = thread_bs_id
        self.name = name
        self.clock_max = clock_max
        self.bx_pointer = 0

    def run(self):
        print ("开启线程： " + self.name)
        # 进行数据共享交换
        clock = random.randint(1, 20)
        while clock < self.clock_max:
            '''当前时刻判断当前业务是否发生，若发生则按较短的时间间隔进行其包含的行为；否则间隔随机一段时间再判断当前业务是否发生'''
            pro = random.random()
            if pro >= 0.7:
                clock, self.bx_pointer = bx_happening(clock, self.thread_bs_id, self.bx_pointer)
                clock += random.randint(exec_wait_interval_min, exec_wait_interval_max)
            else:
                clock += random.randint(bs_inter_min, bs_inter_max)


def bx_happening(clock, bs_id, bx_pointer):
    '''发生当前业务，按较短时间间隔推进当前协同业务包含的行为'''
    while True:
        pro = random.random()
        if pro >= 0.5:
            # 在区块链中记录当前数据行为，行为序号最后按时间戳排序之后加入
            cur_bx = []
            cur_bx.append(clock // sec_per_block)   # 添加block_id
            sec = round(random.random(), 3)
            cur_bx.append(clock+sec)            # 添加时间戳
            cur_bx_paradigm_id = bs_info[bs_id][bx_pointer % len(bs_info[bs_id])]    # 添加当前行为范式ID
            cur_bx.append(cur_bx_paradigm_id)
            cur_bx.append(random.choice(bx_paradigm_info[cur_bx_paradigm_id][-1]))
            # 生成数据量
            data_volume = []
            if bx_paradigm_info[cur_bx_paradigm_id][1] == 1:
                for i in range(len(bx_paradigm_info[cur_bx_paradigm_id][-1])):
                    data_volume.append(random.randint(1, max_data_volume))
            else:
                data_volume.append(random.randint(1, max_data_volume))
            cur_bx.append(data_volume)
            # 获取锁，用于线程同步
            threadLock.acquire()
            bs_seq.append((clock+sec, bs_id))
            bx_seq_dataset.append(cur_bx)
            # 释放锁，开启下一个线程
            threadLock.release()
            bx_pointer += 1
        clock += 1
        if bx_pointer != 0 and bs_info[bs_id][bx_pointer % len(bs_info[bs_id])] == bs_info[bs_id][0]:
            break
    return clock, bx_pointer

def take_timestamp_bs_seq(elem):
    return elem[0]

def take_timestamp_bx_seq(elem):
    return elem[1]

# 读取业务场景数据行为序列
filename_pkl = 'scenario 01\\03 bs.pkl'
with open(filename_pkl, 'rb') as file_obj:
    bs_info = pickle.load(file_obj)
bs_num = len(bs_info)

# 读取数据行为范式信息
filename_pkl = 'scenario 01\\02 bx_paradigm_info.pkl'
with open(filename_pkl, 'rb') as file_obj:
    bx_paradigm_info = pickle.load(file_obj)

bs_pointer = [0 for i in range(bs_num)]     # 初始化每个业务场景的指针
bx_seq_dataset = []         # 数据集(block_ID,Bx_seqNum,timestamp,Bx_paradigm_ID,requesterID,data_volume)
bs_seq = []                 # 对应的业务场景序列
clock_max = 25000
sec_per_block = 50          # 每sec_per_block出一个新区块
max_data_volume = 10        # 设置最大数据量

bs_inter_min = 10           # 当前时刻不发生业务的再次询问时间间隔
bs_inter_max = 20

exec_wait_interval_min = 30     # 业务发生后强制推迟时间，相同业务执行的间隔增大
exec_wait_interval_max = 40

threadLock = threading.Lock()
threads = []
# 创建线程
for i in range(bs_num):
    t = myThread(i, "Thread-"+str(i), clock_max)
    threads.append(t)

# 开启线程
for t in threads:
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")

# 两个二维列表按一维列表/元组中的某个位置的元素进行排序
bs_seq.sort(key=take_timestamp_bs_seq)
bx_seq_dataset.sort(key=take_timestamp_bx_seq)

# bx_seq_dataset加入交易序号
for i in range(len(bx_seq_dataset)):
    bx_seq_dataset[i].insert(1, i)


# print(bs_seq)     # bs_seq: [(4.27, 3), (7.652, 3), (8.946, 3), (9.46, 3), (14.864, 3),...,]
# print(bx_seq_dataset)

filename_pkl = 'scenario 01\\04 bs_seq.pkl'
with open(filename_pkl, 'wb') as file_obj:
    pickle.dump(bs_seq, file_obj)

# 写入txt文件，方便查看
filename = 'scenario 01\\04 bs_seq.txt'
with open(filename, 'w') as file_obj:
    for each in bs_seq:
        for i in range(len(each)):
            file_obj.write(str(int(each[i])))
            if i == len(each) - 1:
                file_obj.write('\n')
            else:
                file_obj.write(' ')

filename_pkl = 'scenario 01\\04 bx_seq_dataset.pkl'
with open(filename_pkl, 'wb') as file_obj:
    pickle.dump(bx_seq_dataset, file_obj)

filename = 'scenario 01\\04 bx_seq_dataset.txt'
with open(filename, 'w') as file_obj:
    for each in bx_seq_dataset:
        for i in range(len(each)):
            file_obj.write(str(each[i]))
            if i == len(each) - 1:
                file_obj.write('\n')
            else:
                file_obj.write(' ')
