# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 20:20:36 2023

@author: shida
"""

import numpy as np
import pandas as pd

'''
ori_regret_ratio_pure = np.loadtxt('./500users_100dims/regret_ratio/RegretRatio_Pure_n100_T_100000')

ori_regret_ratio_rp = np.loadtxt('./500users_100dims/regret_ratio/RegretRatio_RP_n100_T_100000')

ori_regret_ratio_noise = np.loadtxt('./500users_100dims/regret_ratio/RegretRatio_Noise_n100_T_100000')

ori_regret_ratio_op_noise = np.loadtxt('./500users_100dims/regret_ratio/RegretRatio_RP_Noise_n100_T_100000')




new_regret_ratio_pure = np.loadtxt('./500users_100dims_v1/regret_ratio/RegretRatio_Pure_n100_T_100000')

new_regret_ratio_rp = np.loadtxt('./500users_100dims_v1/regret_ratio/RegretRatio_RP_n100_T_100000')

new_regret_ratio_noise = np.loadtxt('./500users_100dims_v1/regret_ratio/RegretRatio_Noise_n100_T_100000')

new_regret_ratio_op_noise = np.loadtxt('./500users_100dims_v1/regret_ratio/RegretRatio_RP_Noise_n100_T_100000')
'''
'''
#结论1：加入贡献度以后，平均regret_ratio更低

regret_ratio_df_pure = pd.DataFrame()
regret_ratio_df_rp = pd.DataFrame()
regret_pure = pd.DataFrame()
regret_rp = pd.DataFrame()

regret_ratio_df_pure['regret_ratio_pure'] = np.loadtxt('./500users_100dims/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure['regret_ratio_pure_v1'] = np.loadtxt('./500users_100dims_v1/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure['regret_ratio_pure_v2'] = np.loadtxt('./500users_100dims_v2/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure['regret_ratio_pure_v3'] = np.loadtxt('./500users_100dims_v3/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure['regret_ratio_pure_v4_1'] = np.loadtxt('./500users_100dims_v4_0.010000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure['regret_ratio_pure_v4_2'] = np.loadtxt('./500users_100dims_v4_0.100000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')


for col in regret_ratio_df_pure.columns:
    print(col, np.mean(regret_ratio_df_pure[col]))
    print(col, np.std(regret_ratio_df_pure[col]))

print('\n')

regret_ratio_df_rp['regret_ratio_rp'] = np.loadtxt('./500users_100dims/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp['regret_ratio_rp_v1'] = np.loadtxt('./500users_100dims_v1/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp['regret_ratio_rp_v2'] = np.loadtxt('./500users_100dims_v2/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp['regret_ratio_rp_v3'] = np.loadtxt('./500users_100dims_v3/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp['regret_ratio_rp_v4_1'] = np.loadtxt('./500users_100dims_v4_0.010000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp['regret_ratio_rp_v4_2'] = np.loadtxt('./500users_100dims_v4_0.100000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')


for col in regret_ratio_df_rp.columns:
    print(col, np.mean(regret_ratio_df_rp[col]))
    print(col, np.std(regret_ratio_df_rp[col]))

print('\n')


regret_pure['regret_pure'] = np.loadtxt('./500users_100dims/regret_total/TotalRegrets_n100_T_100000')
regret_pure['regret_pure_v1'] = np.loadtxt('./500users_100dims_v1/regret_total/TotalRegrets_n100_T_100000')
regret_pure['regret_pure_v2'] = np.loadtxt('./500users_100dims_v2/regret_total/TotalRegrets_n100_T_100000')
regret_pure['regret_pure_v3'] = np.loadtxt('./500users_100dims_v3/regret_total/TotalRegrets_n100_T_100000')
regret_pure['regret_pure_v4_1'] = np.loadtxt('./500users_100dims_v4_0.010000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_pure['regret_pure_v4_2'] = np.loadtxt('./500users_100dims_v4_0.100000alpha/regret_total/TotalRegrets_n100_T_100000')


for col in regret_pure.columns:
    print(col, np.mean(regret_pure[col]))
    print(col, np.std(regret_pure[col]))

print('\n')


regret_rp['regret_rp'] = np.loadtxt('./500users_100dims/regret_total/TotalRegrets_RP_n100_T_100000')
regret_rp['regret_rp_v1'] = np.loadtxt('./500users_100dims_v1/regret_total/TotalRegrets_RP_n100_T_100000')
regret_rp['regret_rp_v2'] = np.loadtxt('./500users_100dims_v2/regret_total/TotalRegrets_RP_n100_T_100000')
regret_rp['regret_rp_v3'] = np.loadtxt('./500users_100dims_v3/regret_total/TotalRegrets_RP_n100_T_100000')
regret_rp['regret_rp_v4_1'] = np.loadtxt('./500users_100dims_v4_0.010000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_rp['regret_rp_v4_2'] = np.loadtxt('./500users_100dims_v4_0.100000alpha/regret_total/TotalRegrets_RP_n100_T_100000')


for col in regret_rp.columns:
    print(col, np.mean(regret_rp[col]))
    print(col, np.std(regret_rp[col]))

regret_pure.to_csv('n100_T_100000_regret_pure.csv',index=None)


'''
'''
V1：隐私补偿    L2-norm
V2：隐私补偿    L1-norm
V3：隐私补偿+贡献度    L2-norm
V4：隐私补偿    L1-norm + 贡献度
V5：隐私补偿    L2-norm + 贡献度

series
1: regret_weight = 1.0
2: regret_weight = 0.1
3: regret_weight = 0.5
'''

'''

regret_ratio_df_pure1 = pd.DataFrame()
regret_ratio_df_rp1 = pd.DataFrame()



regret_ratio_df_pure1['regret_ratio_pure_v1'] = np.loadtxt('./regret_weight1.0/500users_100dims_v1/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure1['regret_ratio_pure_v2'] = np.loadtxt('./regret_weight1.0/500users_100dims_v2/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure1['regret_ratio_pure_v3_alpha1.0'] = np.loadtxt('./regret_weight1.0/500users_100dims_v3_1.000000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure1['regret_ratio_pure_v4_alpha1.0'] = np.loadtxt('./regret_weight1.0/500users_100dims_v4_1.000000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure1['regret_ratio_pure_v5_alpha1.0'] = np.loadtxt('./regret_weight1.0/500users_100dims_v5_1.000000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')

regret_ratio_df_pure1['regret_ratio_pure_v3_alpha0.1'] = np.loadtxt('./regret_weight1.0/500users_100dims_v3_0.100000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure1['regret_ratio_pure_v4_alpha0.1'] = np.loadtxt('./regret_weight1.0/500users_100dims_v4_0.100000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure1['regret_ratio_pure_v5_alpha0.1'] = np.loadtxt('./regret_weight1.0/500users_100dims_v5_0.100000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')

regret_ratio_df_pure1['regret_ratio_pure_v3_alpha0.01'] = np.loadtxt('./regret_weight1.0/500users_100dims_v3_0.010000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure1['regret_ratio_pure_v4_alpha0.01'] = np.loadtxt('./regret_weight1.0/500users_100dims_v4_0.010000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure1['regret_ratio_pure_v5_alpha0.01'] = np.loadtxt('./regret_weight1.0/500users_100dims_v5_0.010000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')




regret_ratio_df_rp1['regret_ratio_rp_v1'] = np.loadtxt('./regret_weight1.0/500users_100dims_v1/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp1['regret_ratio_rp_v2'] = np.loadtxt('./regret_weight1.0/500users_100dims_v2/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp1['regret_ratio_rp_v3_alpha1.0'] = np.loadtxt('./regret_weight1.0/500users_100dims_v3_1.000000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp1['regret_ratio_rp_v4_alpha1.0'] = np.loadtxt('./regret_weight1.0/500users_100dims_v4_1.000000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp1['regret_ratio_rp_v5_alpha1.0'] = np.loadtxt('./regret_weight1.0/500users_100dims_v5_1.000000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')

regret_ratio_df_rp1['regret_ratio_rp_v3_alpha0.1'] = np.loadtxt('./regret_weight1.0/500users_100dims_v3_0.100000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp1['regret_ratio_rp_v4_alpha0.1'] = np.loadtxt('./regret_weight1.0/500users_100dims_v4_0.100000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp1['regret_ratio_rp_v5_alpha0.1'] = np.loadtxt('./regret_weight1.0/500users_100dims_v5_0.100000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')

regret_ratio_df_rp1['regret_ratio_rp_v3_alpha0.01'] = np.loadtxt('./regret_weight1.0/500users_100dims_v3_0.010000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp1['regret_ratio_rp_v4_alpha0.01'] = np.loadtxt('./regret_weight1.0/500users_100dims_v4_0.010000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp1['regret_ratio_rp_v5_alpha0.01'] = np.loadtxt('./regret_weight1.0/500users_100dims_v5_0.010000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')




regret_total_df_pure1 = pd.DataFrame()
regret_total_df_rp1 = pd.DataFrame()



regret_total_df_pure1['regret_total_pure_v1'] = np.loadtxt('./regret_weight1.0/500users_100dims_v1/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure1['regret_total_pure_v2'] = np.loadtxt('./regret_weight1.0/500users_100dims_v2/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure1['regret_total_pure_v3_alpha1.0'] = np.loadtxt('./regret_weight1.0/500users_100dims_v3_1.000000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure1['regret_total_pure_v4_alpha1.0'] = np.loadtxt('./regret_weight1.0/500users_100dims_v4_1.000000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure1['regret_total_pure_v5_alpha1.0'] = np.loadtxt('./regret_weight1.0/500users_100dims_v5_1.000000alpha/regret_total/TotalRegrets_n100_T_100000')

regret_total_df_pure1['regret_total_pure_v3_alpha0.1'] = np.loadtxt('./regret_weight1.0/500users_100dims_v3_0.100000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure1['regret_total_pure_v4_alpha0.1'] = np.loadtxt('./regret_weight1.0/500users_100dims_v4_0.100000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure1['regret_total_pure_v5_alpha0.1'] = np.loadtxt('./regret_weight1.0/500users_100dims_v5_0.100000alpha/regret_total/TotalRegrets_n100_T_100000')

regret_total_df_pure1['regret_total_pure_v3_alpha0.01'] = np.loadtxt('./regret_weight1.0/500users_100dims_v3_0.010000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure1['regret_total_pure_v4_alpha0.01'] = np.loadtxt('./regret_weight1.0/500users_100dims_v4_0.010000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure1['regret_total_pure_v5_alpha0.01'] = np.loadtxt('./regret_weight1.0/500users_100dims_v5_0.010000alpha/regret_total/TotalRegrets_n100_T_100000')



regret_total_df_rp1['regret_total_rp_v1'] = np.loadtxt('./regret_weight1.0/500users_100dims_v1/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp1['regret_total_rp_v2'] = np.loadtxt('./regret_weight1.0/500users_100dims_v2/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp1['regret_total_rp_v3_alpha1.0'] = np.loadtxt('./regret_weight1.0/500users_100dims_v3_1.000000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp1['regret_total_rp_v4_alpha1.0'] = np.loadtxt('./regret_weight1.0/500users_100dims_v4_1.000000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp1['regret_total_rp_v5_alpha1.0'] = np.loadtxt('./regret_weight1.0/500users_100dims_v5_1.000000alpha/regret_total/TotalRegrets_RP_n100_T_100000')

regret_total_df_rp1['regret_total_rp_v3_alpha0.1'] = np.loadtxt('./regret_weight1.0/500users_100dims_v3_0.100000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp1['regret_total_rp_v4_alpha0.1'] = np.loadtxt('./regret_weight1.0/500users_100dims_v4_0.100000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp1['regret_total_rp_v5_alpha0.1'] = np.loadtxt('./regret_weight1.0/500users_100dims_v5_0.100000alpha/regret_total/TotalRegrets_RP_n100_T_100000')

regret_total_df_rp1['regret_total_rp_v3_alpha0.01'] = np.loadtxt('./regret_weight1.0/500users_100dims_v3_0.010000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp1['regret_total_rp_v4_alpha0.01'] = np.loadtxt('./regret_weight1.0/500users_100dims_v4_0.010000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp1['regret_total_rp_v5_alpha0.01'] = np.loadtxt('./regret_weight1.0/500users_100dims_v5_0.010000alpha/regret_total/TotalRegrets_RP_n100_T_100000')




regret_ratio_df_pure2 = pd.DataFrame()
regret_ratio_df_rp2 = pd.DataFrame()


regret_ratio_df_pure2['regret_ratio_pure_v1'] = np.loadtxt('./regret_weight0.1/500users_100dims_v1/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure2['regret_ratio_pure_v2'] = np.loadtxt('./regret_weight0.1/500users_100dims_v2/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure2['regret_ratio_pure_v3_alpha1.0'] = np.loadtxt('./regret_weight0.1/500users_100dims_v3_1.000000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure2['regret_ratio_pure_v4_alpha1.0'] = np.loadtxt('./regret_weight0.1/500users_100dims_v4_1.000000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure2['regret_ratio_pure_v5_alpha1.0'] = np.loadtxt('./regret_weight0.1/500users_100dims_v5_1.000000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')

regret_ratio_df_pure2['regret_ratio_pure_v3_alpha0.1'] = np.loadtxt('./regret_weight0.1/500users_100dims_v3_0.100000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure2['regret_ratio_pure_v4_alpha0.1'] = np.loadtxt('./regret_weight0.1/500users_100dims_v4_0.100000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure2['regret_ratio_pure_v5_alpha0.1'] = np.loadtxt('./regret_weight0.1/500users_100dims_v5_0.100000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')

regret_ratio_df_pure2['regret_ratio_pure_v3_alpha0.01'] = np.loadtxt('./regret_weight0.1/500users_100dims_v3_0.010000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure2['regret_ratio_pure_v4_alpha0.01'] = np.loadtxt('./regret_weight0.1/500users_100dims_v4_0.010000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure2['regret_ratio_pure_v5_alpha0.01'] = np.loadtxt('./regret_weight0.1/500users_100dims_v5_0.010000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')




regret_ratio_df_rp2['regret_ratio_rp_v1'] = np.loadtxt('./regret_weight0.1/500users_100dims_v1/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp2['regret_ratio_rp_v2'] = np.loadtxt('./regret_weight0.1/500users_100dims_v2/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp2['regret_ratio_rp_v3_alpha1.0'] = np.loadtxt('./regret_weight0.1/500users_100dims_v3_1.000000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp2['regret_ratio_rp_v4_alpha1.0'] = np.loadtxt('./regret_weight0.1/500users_100dims_v4_1.000000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp2['regret_ratio_rp_v5_alpha1.0'] = np.loadtxt('./regret_weight0.1/500users_100dims_v5_1.000000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')

regret_ratio_df_rp2['regret_ratio_rp_v3_alpha0.1'] = np.loadtxt('./regret_weight0.1/500users_100dims_v3_0.100000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp2['regret_ratio_rp_v4_alpha0.1'] = np.loadtxt('./regret_weight0.1/500users_100dims_v4_0.100000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp2['regret_ratio_rp_v5_alpha0.1'] = np.loadtxt('./regret_weight0.1/500users_100dims_v5_0.100000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')

regret_ratio_df_rp2['regret_ratio_rp_v3_alpha0.01'] = np.loadtxt('./regret_weight0.1/500users_100dims_v3_0.010000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp2['regret_ratio_rp_v4_alpha0.01'] = np.loadtxt('./regret_weight0.1/500users_100dims_v4_0.010000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp2['regret_ratio_rp_v5_alpha0.01'] = np.loadtxt('./regret_weight0.1/500users_100dims_v5_0.010000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')




regret_total_df_pure2 = pd.DataFrame()
regret_total_df_rp2 = pd.DataFrame()


regret_total_df_pure2['regret_total_pure_v1'] = np.loadtxt('./regret_weight0.1/500users_100dims_v1/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure2['regret_total_pure_v2'] = np.loadtxt('./regret_weight0.1/500users_100dims_v2/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure2['regret_total_pure_v3_alpha1.0'] = np.loadtxt('./regret_weight0.1/500users_100dims_v3_1.000000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure2['regret_total_pure_v4_alpha1.0'] = np.loadtxt('./regret_weight0.1/500users_100dims_v4_1.000000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure2['regret_total_pure_v5_alpha1.0'] = np.loadtxt('./regret_weight0.1/500users_100dims_v5_1.000000alpha/regret_total/TotalRegrets_n100_T_100000')

regret_total_df_pure2['regret_total_pure_v3_alpha0.1'] = np.loadtxt('./regret_weight0.1/500users_100dims_v3_0.100000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure2['regret_total_pure_v4_alpha0.1'] = np.loadtxt('./regret_weight0.1/500users_100dims_v4_0.100000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure2['regret_total_pure_v5_alpha0.1'] = np.loadtxt('./regret_weight0.1/500users_100dims_v5_0.100000alpha/regret_total/TotalRegrets_n100_T_100000')

regret_total_df_pure2['regret_total_pure_v3_alpha0.01'] = np.loadtxt('./regret_weight0.1/500users_100dims_v3_0.010000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure2['regret_total_pure_v4_alpha0.01'] = np.loadtxt('./regret_weight0.1/500users_100dims_v4_0.010000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure2['regret_total_pure_v5_alpha0.01'] = np.loadtxt('./regret_weight0.1/500users_100dims_v5_0.010000alpha/regret_total/TotalRegrets_n100_T_100000')



regret_total_df_rp2['regret_total_rp_v1'] = np.loadtxt('./regret_weight0.1/500users_100dims_v1/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp2['regret_total_rp_v2'] = np.loadtxt('./regret_weight0.1/500users_100dims_v2/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp2['regret_total_rp_v3_alpha1.0'] = np.loadtxt('./regret_weight0.1/500users_100dims_v3_1.000000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp2['regret_total_rp_v4_alpha1.0'] = np.loadtxt('./regret_weight0.1/500users_100dims_v4_1.000000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp2['regret_total_rp_v5_alpha1.0'] = np.loadtxt('./regret_weight0.1/500users_100dims_v5_1.000000alpha/regret_total/TotalRegrets_RP_n100_T_100000')

regret_total_df_rp2['regret_total_rp_v3_alpha0.1'] = np.loadtxt('./regret_weight0.1/500users_100dims_v3_0.100000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp2['regret_total_rp_v4_alpha0.1'] = np.loadtxt('./regret_weight0.1/500users_100dims_v4_0.100000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp2['regret_total_rp_v5_alpha0.1'] = np.loadtxt('./regret_weight0.1/500users_100dims_v5_0.100000alpha/regret_total/TotalRegrets_RP_n100_T_100000')

regret_total_df_rp2['regret_total_rp_v3_alpha0.01'] = np.loadtxt('./regret_weight0.1/500users_100dims_v3_0.010000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp2['regret_total_rp_v4_alpha0.01'] = np.loadtxt('./regret_weight0.1/500users_100dims_v4_0.010000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp2['regret_total_rp_v5_alpha0.01'] = np.loadtxt('./regret_weight0.1/500users_100dims_v5_0.010000alpha/regret_total/TotalRegrets_RP_n100_T_100000')



regret_ratio_df_pure3 = pd.DataFrame()
regret_ratio_df_rp3 = pd.DataFrame()


regret_ratio_df_pure3['regret_ratio_pure_v1'] = np.loadtxt('./regret_weight0.5/500users_100dims_v1/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure3['regret_ratio_pure_v2'] = np.loadtxt('./regret_weight0.5/500users_100dims_v2/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure3['regret_ratio_pure_v3_alpha1.0'] = np.loadtxt('./regret_weight0.5/500users_100dims_v3_1.000000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure3['regret_ratio_pure_v4_alpha1.0'] = np.loadtxt('./regret_weight0.5/500users_100dims_v4_1.000000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure3['regret_ratio_pure_v5_alpha1.0'] = np.loadtxt('./regret_weight0.5/500users_100dims_v5_1.000000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')

regret_ratio_df_pure3['regret_ratio_pure_v3_alpha0.1'] = np.loadtxt('./regret_weight0.5/500users_100dims_v3_0.100000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure3['regret_ratio_pure_v4_alpha0.1'] = np.loadtxt('./regret_weight0.5/500users_100dims_v4_0.100000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure3['regret_ratio_pure_v5_alpha0.1'] = np.loadtxt('./regret_weight0.5/500users_100dims_v5_0.100000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')

regret_ratio_df_pure3['regret_ratio_pure_v3_alpha0.01'] = np.loadtxt('./regret_weight0.5/500users_100dims_v3_0.010000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure3['regret_ratio_pure_v4_alpha0.01'] = np.loadtxt('./regret_weight0.5/500users_100dims_v4_0.010000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure3['regret_ratio_pure_v5_alpha0.01'] = np.loadtxt('./regret_weight0.5/500users_100dims_v5_0.010000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')




regret_ratio_df_rp3['regret_ratio_rp_v1'] = np.loadtxt('./regret_weight0.5/500users_100dims_v1/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp3['regret_ratio_rp_v2'] = np.loadtxt('./regret_weight0.5/500users_100dims_v2/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp3['regret_ratio_rp_v3_alpha1.0'] = np.loadtxt('./regret_weight0.5/500users_100dims_v3_1.000000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp3['regret_ratio_rp_v4_alpha1.0'] = np.loadtxt('./regret_weight0.5/500users_100dims_v4_1.000000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp3['regret_ratio_rp_v5_alpha1.0'] = np.loadtxt('./regret_weight0.5/500users_100dims_v5_1.000000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')

regret_ratio_df_rp3['regret_ratio_rp_v3_alpha0.1'] = np.loadtxt('./regret_weight0.5/500users_100dims_v3_0.100000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp3['regret_ratio_rp_v4_alpha0.1'] = np.loadtxt('./regret_weight0.5/500users_100dims_v4_0.100000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp3['regret_ratio_rp_v5_alpha0.1'] = np.loadtxt('./regret_weight0.5/500users_100dims_v5_0.100000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')

regret_ratio_df_rp3['regret_ratio_rp_v3_alpha0.01'] = np.loadtxt('./regret_weight0.5/500users_100dims_v3_0.010000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp3['regret_ratio_rp_v4_alpha0.01'] = np.loadtxt('./regret_weight0.5/500users_100dims_v4_0.010000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp3['regret_ratio_rp_v5_alpha0.01'] = np.loadtxt('./regret_weight0.5/500users_100dims_v5_0.010000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')




regret_total_df_pure3 = pd.DataFrame()
regret_total_df_rp3 = pd.DataFrame()


regret_total_df_pure3['regret_total_pure_v1'] = np.loadtxt('./regret_weight0.5/500users_100dims_v1/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure3['regret_total_pure_v2'] = np.loadtxt('./regret_weight0.5/500users_100dims_v2/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure3['regret_total_pure_v3_alpha1.0'] = np.loadtxt('./regret_weight0.5/500users_100dims_v3_1.000000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure3['regret_total_pure_v4_alpha1.0'] = np.loadtxt('./regret_weight0.5/500users_100dims_v4_1.000000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure3['regret_total_pure_v5_alpha1.0'] = np.loadtxt('./regret_weight0.5/500users_100dims_v5_1.000000alpha/regret_total/TotalRegrets_n100_T_100000')

regret_total_df_pure3['regret_total_pure_v3_alpha0.1'] = np.loadtxt('./regret_weight0.5/500users_100dims_v3_0.100000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure3['regret_total_pure_v4_alpha0.1'] = np.loadtxt('./regret_weight0.5/500users_100dims_v4_0.100000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure3['regret_total_pure_v5_alpha0.1'] = np.loadtxt('./regret_weight0.5/500users_100dims_v5_0.100000alpha/regret_total/TotalRegrets_n100_T_100000')

regret_total_df_pure3['regret_total_pure_v3_alpha0.01'] = np.loadtxt('./regret_weight0.5/500users_100dims_v3_0.010000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure3['regret_total_pure_v4_alpha0.01'] = np.loadtxt('./regret_weight0.5/500users_100dims_v4_0.010000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure3['regret_total_pure_v5_alpha0.01'] = np.loadtxt('./regret_weight0.5/500users_100dims_v5_0.010000alpha/regret_total/TotalRegrets_n100_T_100000')



regret_total_df_rp3['regret_total_rp_v1'] = np.loadtxt('./regret_weight0.5/500users_100dims_v1/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp3['regret_total_rp_v2'] = np.loadtxt('./regret_weight0.5/500users_100dims_v2/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp3['regret_total_rp_v3_alpha1.0'] = np.loadtxt('./regret_weight0.5/500users_100dims_v3_1.000000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp3['regret_total_rp_v4_alpha1.0'] = np.loadtxt('./regret_weight0.5/500users_100dims_v4_1.000000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp3['regret_total_rp_v5_alpha1.0'] = np.loadtxt('./regret_weight0.5/500users_100dims_v5_1.000000alpha/regret_total/TotalRegrets_RP_n100_T_100000')

regret_total_df_rp3['regret_total_rp_v3_alpha0.1'] = np.loadtxt('./regret_weight0.5/500users_100dims_v3_0.100000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp3['regret_total_rp_v4_alpha0.1'] = np.loadtxt('./regret_weight0.5/500users_100dims_v4_0.100000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp3['regret_total_rp_v5_alpha0.1'] = np.loadtxt('./regret_weight0.5/500users_100dims_v5_0.100000alpha/regret_total/TotalRegrets_RP_n100_T_100000')

regret_total_df_rp3['regret_total_rp_v3_alpha0.01'] = np.loadtxt('./regret_weight0.5/500users_100dims_v3_0.010000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp3['regret_total_rp_v4_alpha0.01'] = np.loadtxt('./regret_weight0.5/500users_100dims_v4_0.010000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp3['regret_total_rp_v5_alpha0.01'] = np.loadtxt('./regret_weight0.5/500users_100dims_v5_0.010000alpha/regret_total/TotalRegrets_RP_n100_T_100000')

'''

'''
df_write2 = pd.DataFrame(data = list(range(1,100001)), columns = ['rounds'])
df_write2['regret_total_privacy_l2norm'] = regret_total_df_pure1['regret_total_pure_v1']
df_write2['regret_total_privacy_l1norm'] = regret_total_df_pure1['regret_total_pure_v2']
df_write2['regret_total_privacy-contribution_l2norm'] = regret_total_df_pure1['regret_total_pure_v3_alpha1.0']
df_write2['regret_total_privacy-l1norm_contribution'] = regret_total_df_pure1['regret_total_pure_v4_alpha1.0']
df_write2['regret_total_privacy-l2norm_contribution'] = regret_total_df_pure1['regret_total_pure_v5_alpha1.0']

df_write2.to_csv('plot_norm.csv',index=None)
'''

'''
df_write1 = pd.DataFrame()
df_write1['rounds'] = list(range(1,100001))
#df_write1['regret_total_pure_v1'] = regret_total_df_pure1['regret_total_pure_v1']
#df_write1['regret_total_pure_v2'] = regret_total_df_pure2['regret_total_pure_v2']

df_write1['regret_weight1.0'] = regret_total_df_pure1['regret_total_pure_v1']
df_write1['regret_weight0.5'] = regret_total_df_pure3['regret_total_pure_v1']
df_write1['regret_weight0.1'] = regret_total_df_pure2['regret_total_pure_v1']

df_write1.to_csv('plot_regret_weight.csv',index=None)




df_write3 = pd.DataFrame(data = list(range(1,100001)), columns = ['rounds'])
df_write3['regret_ratio_pure_v1'] = regret_ratio_df_pure1['regret_ratio_pure_v1']
df_write3['regret_ratio_pure_v2'] = regret_ratio_df_pure1['regret_ratio_pure_v2']
df_write3['regret_ratio_pure_v3'] = regret_ratio_df_pure1['regret_ratio_pure_v3_alpha1.0']
df_write3['regret_ratio_pure_v4'] = regret_ratio_df_pure1['regret_ratio_pure_v4_alpha1.0']
df_write3['regret_ratio_pure_v5'] = regret_ratio_df_pure1['regret_ratio_pure_v5_alpha1.0']

df_write3.to_csv('plot_regret_ratio.csv',index=None)



df_write4 = pd.DataFrame(data = list(range(1,100001)), columns = ['rounds'])
df_write4['regret_total_pure_v1'] = regret_total_df_pure1['regret_total_pure_v1']
df_write4['regret_total_contribution_alpha1.00'] = regret_total_df_pure1['regret_total_pure_v5_alpha1.0']
df_write4['regret_total_contribution_alpha0.10'] = regret_total_df_pure1['regret_total_pure_v5_alpha0.1']
df_write4['regret_total_contribution_alpha0.01'] = regret_total_df_pure1['regret_total_pure_v5_alpha0.01']

df_write4.to_csv('plot_contribution_alpha1.csv',index=None)

'''
'''

#减少累积regret
regret_total_df_pure1 = pd.DataFrame()

regret_total_df_pure1['regret_total_pure_v1'] = np.loadtxt('./regret_weight1.0/200users_100dims_v1/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure1['regret_total_pure_v2_alpha1.0'] = np.loadtxt('./regret_weight1.0/200users_100dims_v2_1.000000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure1['regret_total_pure_v3_alpha1.0'] = np.loadtxt('./regret_weight1.0/200users_100dims_v3_1.000000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure1['regret_total_pure_v4_alpha1.0'] = np.loadtxt('./regret_weight1.0/200users_100dims_v4_1.000000alpha/regret_total/TotalRegrets_n100_T_100000')

regret_total_df_pure1['regret_total_pure_v2_alpha0.1'] = np.loadtxt('./regret_weight1.0/200users_100dims_v2_0.100000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure1['regret_total_pure_v3_alpha0.1'] = np.loadtxt('./regret_weight1.0/200users_100dims_v3_0.100000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure1['regret_total_pure_v4_alpha0.1'] = np.loadtxt('./regret_weight1.0/200users_100dims_v4_0.100000alpha/regret_total/TotalRegrets_n100_T_100000')

regret_total_df_pure1['regret_total_pure_v2_alpha0.01'] = np.loadtxt('./regret_weight1.0/200users_100dims_v2_0.010000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure1['regret_total_pure_v3_alpha0.01'] = np.loadtxt('./regret_weight1.0/200users_100dims_v3_0.010000alpha/regret_total/TotalRegrets_n100_T_100000')
regret_total_df_pure1['regret_total_pure_v4_alpha0.01'] = np.loadtxt('./regret_weight1.0/200users_100dims_v4_0.010000alpha/regret_total/TotalRegrets_n100_T_100000')


regret_total_df_rp1 = pd.DataFrame()
regret_total_df_rp1['regret_total_rp_v1'] = np.loadtxt('./regret_weight1.0/200users_100dims_v1/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp1['regret_total_rp_v2_alpha1.0'] = np.loadtxt('./regret_weight1.0/200users_100dims_v2_1.000000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp1['regret_total_rp_v3_alpha1.0'] = np.loadtxt('./regret_weight1.0/200users_100dims_v3_1.000000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp1['regret_total_rp_v4_alpha1.0'] = np.loadtxt('./regret_weight1.0/200users_100dims_v4_1.000000alpha/regret_total/TotalRegrets_RP_n100_T_100000')

regret_total_df_rp1['regret_total_rp_v2_alpha0.1'] = np.loadtxt('./regret_weight1.0/200users_100dims_v2_0.100000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp1['regret_total_rp_v3_alpha0.1'] = np.loadtxt('./regret_weight1.0/200users_100dims_v3_0.100000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp1['regret_total_rp_v4_alpha0.1'] = np.loadtxt('./regret_weight1.0/200users_100dims_v4_0.100000alpha/regret_total/TotalRegrets_RP_n100_T_100000')

regret_total_df_rp1['regret_total_rp_v2_alpha0.01'] = np.loadtxt('./regret_weight1.0/200users_100dims_v2_0.010000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp1['regret_total_rp_v3_alpha0.01'] = np.loadtxt('./regret_weight1.0/200users_100dims_v3_0.010000alpha/regret_total/TotalRegrets_RP_n100_T_100000')
regret_total_df_rp1['regret_total_rp_v4_alpha0.01'] = np.loadtxt('./regret_weight1.0/200users_100dims_v4_0.010000alpha/regret_total/TotalRegrets_RP_n100_T_100000')


regret_ratio_df_pure1 = pd.DataFrame()
regret_ratio_df_rp1 = pd.DataFrame()



regret_ratio_df_pure1['regret_ratio_pure_v1'] = np.loadtxt('./regret_weight1.0/200users_100dims_v1/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure1['regret_ratio_pure_v2_alpha1.0'] = np.loadtxt('./regret_weight1.0/200users_100dims_v2_1.000000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure1['regret_ratio_pure_v3_alpha1.0'] = np.loadtxt('./regret_weight1.0/200users_100dims_v3_1.000000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure1['regret_ratio_pure_v4_alpha1.0'] = np.loadtxt('./regret_weight1.0/200users_100dims_v4_1.000000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')

regret_ratio_df_pure1['regret_ratio_pure_v2_alpha0.1'] = np.loadtxt('./regret_weight1.0/200users_100dims_v2_0.100000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure1['regret_ratio_pure_v3_alpha0.1'] = np.loadtxt('./regret_weight1.0/200users_100dims_v3_0.100000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure1['regret_ratio_pure_v4_alpha0.1'] = np.loadtxt('./regret_weight1.0/200users_100dims_v4_0.100000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')

regret_ratio_df_pure1['regret_ratio_pure_v3_alpha0.01'] = np.loadtxt('./regret_weight1.0/200users_100dims_v2_0.010000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure1['regret_ratio_pure_v4_alpha0.01'] = np.loadtxt('./regret_weight1.0/200users_100dims_v3_0.010000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
regret_ratio_df_pure1['regret_ratio_pure_v5_alpha0.01'] = np.loadtxt('./regret_weight1.0/200users_100dims_v4_0.010000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')




regret_ratio_df_rp1['regret_ratio_rp_v1'] = np.loadtxt('./regret_weight1.0/200users_100dims_v1/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp1['regret_ratio_rp_v2_alpha1.0'] = np.loadtxt('./regret_weight1.0/200users_100dims_v2_1.000000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp1['regret_ratio_rp_v3_alpha1.0'] = np.loadtxt('./regret_weight1.0/200users_100dims_v3_1.000000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp1['regret_ratio_rp_v4_alpha1.0'] = np.loadtxt('./regret_weight1.0/200users_100dims_v4_1.000000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')

regret_ratio_df_rp1['regret_ratio_rp_v2_alpha0.1'] = np.loadtxt('./regret_weight1.0/200users_100dims_v2_0.100000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp1['regret_ratio_rp_v3_alpha0.1'] = np.loadtxt('./regret_weight1.0/200users_100dims_v3_0.100000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp1['regret_ratio_rp_v4_alpha0.1'] = np.loadtxt('./regret_weight1.0/200users_100dims_v4_0.100000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')

regret_ratio_df_rp1['regret_ratio_rp_v2_alpha0.01'] = np.loadtxt('./regret_weight1.0/200users_100dims_v2_0.010000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp1['regret_ratio_rp_v3_alpha0.01'] = np.loadtxt('./regret_weight1.0/200users_100dims_v3_0.010000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')
regret_ratio_df_rp1['regret_ratio_rp_v4_alpha0.01'] = np.loadtxt('./regret_weight1.0/200users_100dims_v4_0.010000alpha/regret_ratio/RegretRatio_RP_n100_T_100000')




df_write1 = pd.DataFrame()
df_write1['rounds'] = list(range(1,100001))

df_write1['methods1'] = regret_total_df_pure1['regret_total_pure_v1']
df_write1['methods2'] = regret_total_df_pure1['regret_total_pure_v2_alpha1.0']
df_write1['methods3'] = regret_total_df_pure1['regret_total_pure_v3_alpha1.0']
df_write1['methods4'] = regret_total_df_pure1['regret_total_pure_v4_alpha1.0']

df_write1.to_csv('plot_total_regret1.csv',index=None)


df_write2 = pd.DataFrame()
df_write2['rounds'] = list(range(1,100001))

df_write2['methods1'] = regret_ratio_df_pure1['regret_ratio_pure_v1']
df_write2['methods2'] = regret_ratio_df_pure1['regret_ratio_pure_v2_alpha1.0']
df_write2['methods3'] = regret_ratio_df_pure1['regret_ratio_pure_v3_alpha1.0']
df_write2['methods4'] = regret_ratio_df_pure1['regret_ratio_pure_v4_alpha1.0']

df_write2.to_csv('plot_regret_ratio1.csv',index=None)



df_write3 = pd.DataFrame()
df_write4 = pd.DataFrame()
df_write5 = pd.DataFrame()

df_write3['rounds'] = list(range(1,100001))
df_write4['rounds'] = list(range(1,100001))
df_write5['rounds'] = list(range(1,100001))

df_write3['methods1'] = regret_total_df_pure1['regret_total_pure_v1']
df_write4['methods1'] = regret_total_df_pure1['regret_total_pure_v1']
df_write5['methods1'] = regret_total_df_pure1['regret_total_pure_v1']

df_write3['methods2_alpha1.0'] = regret_total_df_pure1['regret_total_pure_v2_alpha1.0']
df_write4['methods3_alpha1.0'] = regret_total_df_pure1['regret_total_pure_v3_alpha1.0']
df_write5['methods4_alpha1.0'] = regret_total_df_pure1['regret_total_pure_v4_alpha1.0']

df_write3['methods2_alpha0.1'] = regret_total_df_pure1['regret_total_pure_v2_alpha0.1']
df_write4['methods3_alpha0.1'] = regret_total_df_pure1['regret_total_pure_v3_alpha0.1']
df_write5['methods4_alpha0.1'] = regret_total_df_pure1['regret_total_pure_v4_alpha0.1']

df_write3['methods2_alpha0.01'] = regret_total_df_pure1['regret_total_pure_v2_alpha0.01']
df_write4['methods3_alpha0.01'] = regret_total_df_pure1['regret_total_pure_v3_alpha0.01']
df_write5['methods4_alpha0.01'] = regret_total_df_pure1['regret_total_pure_v4_alpha0.01']

df_write3.to_csv('plot_regret_ratio_alpha1.csv',index=None)
df_write4.to_csv('plot_regret_ratio_alpha2.csv',index=None)
df_write5.to_csv('plot_regret_ratio_alpha3.csv',index=None)



df_write6 = pd.DataFrame()
df_write6['rounds'] = list(range(1,100001))

df_write6['methods2_regret_weight1.0'] = np.loadtxt('./regret_weight1.0/200users_100dims_v2_1.000000alpha/regret_total/TotalRegrets_n100_T_100000')
df_write6['methods2_regret_weight0.5'] = np.loadtxt('./regret_weight0.5/200users_100dims_v2_1.000000alpha/regret_total/TotalRegrets_n100_T_100000')
df_write6['methods2_regret_weight0.1'] = np.loadtxt('./regret_weight0.1/200users_100dims_v2_1.000000alpha/regret_total/TotalRegrets_n100_T_100000')

df_write6.to_csv('plot_regret_weight_methods2.csv',index=None)



df_write7 = pd.DataFrame()
df_write7['rounds'] = list(range(1,100001))

df_write7['methods4_regret_weight1.0'] = np.loadtxt('./regret_weight1.0/200users_100dims_v4_1.000000alpha/regret_total/TotalRegrets_n100_T_100000')
df_write7['methods4_regret_weight0.5'] = np.loadtxt('./regret_weight0.5/200users_100dims_v4_1.000000alpha/regret_total/TotalRegrets_n100_T_100000')
df_write7['methods4_regret_weight0.1'] = np.loadtxt('./regret_weight0.1/200users_100dims_v4_1.000000alpha/regret_total/TotalRegrets_n100_T_100000')

df_write7.to_csv('plot_regret_weight_methods4.csv',index=None)

'''

df_write1 = pd.DataFrame()
df_write1['rounds'] = list(range(1,100001))

df_write1['EBDP'] = np.loadtxt('./200users_100dims_v1/regret_total/TotalRegrets_n100_T_100000')
df_write1['PPIC_alpha2.0'] = np.loadtxt('./200users_100dims_v4_2.000000alpha/regret_total/TotalRegrets_n100_T_100000')
df_write1['PPIC_alpha1.5'] = np.loadtxt('./200users_100dims_v4_1.500000alpha/regret_total/TotalRegrets_n100_T_100000')
df_write1['PPIC_alpha1.0'] = np.loadtxt('./200users_100dims_v4_1.000000alpha/regret_total/TotalRegrets_n100_T_100000')
df_write1['PPIC_alpha0.5'] = np.loadtxt('./200users_100dims_v4_0.500000alpha/regret_total/TotalRegrets_n100_T_100000')
df_write1['PPIC_alpha0.1'] = np.loadtxt('./200users_100dims_v4_0.100000alpha/regret_total/TotalRegrets_n100_T_100000')
mask = (df_write1.index - 99) % 100 == 0

# 使用这个布尔索引来筛选你的DataFrame
df_write1 = df_write1[mask]
df_write1.to_csv('plot_total_regret1.csv',index=None)

df_write2 = pd.DataFrame()
df_write2['rounds'] = list(range(1,100001))

df_write2['EBDP'] = np.loadtxt('./200users_100dims_v1/regret_ratio/RegretRatio_Pure_n100_T_100000')
df_write2['PPIC_alpha2.0'] = np.loadtxt('./200users_100dims_v4_2.000000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
df_write2['PPIC_alpha1.5'] = np.loadtxt('./200users_100dims_v4_1.500000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
df_write2['PPIC_alpha1.0'] = np.loadtxt('./200users_100dims_v4_1.000000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
df_write2['PPIC_alpha0.5'] = np.loadtxt('./200users_100dims_v4_0.500000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
df_write2['PPIC_alpha0.1'] = np.loadtxt('./200users_100dims_v4_0.100000alpha/regret_ratio/RegretRatio_Pure_n100_T_100000')
#mask = (df_write2.index - 99) % 100 == 0

# 使用这个布尔索引来筛选你的DataFrame
# 获取前100个点
first_100_points = df_write2.iloc[:1000]
dfx = df_write2.iloc[1000:].reset_index(drop=True)
# 从第101个点开始，按照给定的条件进行筛选
mask = (dfx.index - 99) % 100 == 0
rest_points = dfx[mask]

# 合并两部分得到的点
selected_points = pd.concat([first_100_points, rest_points])
#df_write2 = df_write2[mask]
#df_write2.to_csv('plot_regret_ratio1.csv',index=None)
selected_points.to_csv('plot_regret_ratio1.csv',index=None)