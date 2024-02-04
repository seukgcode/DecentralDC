"""
@Topic: Pricing of Noisy Linear Query Under Linear Market Value Model
@Usage: Simulate/Generate Online Noisy Linear Queries (Multi-Dimensional)
@Author: Chaoyue Niu
@Email: rvince@sjtu.edu.cn
"""

import numpy as np
import math
from sklearn.preprocessing import normalize
import os
"""
Simulate online linear query 
"""



def Query_feature_vector_v1(N, n, printx):
    #原始的生成算法
    if printx == True:
        print("gen v1 feature vectors")
        print('user_number is %d, feature vector dim is %d\n'%(N, n))
        
    #final feature vctor
    xt = np.zeros((n,1),float)
    #N: the original number of data owners
    #N = 200
    

    #generate "weight vectors" in linear queries
    #multivariate Gaussian distribution (0, I)
    mg_mean = np.zeros(N,float)
    mg_cov = np.identity(N)
    mulGau = np.random.multivariate_normal(mg_mean,mg_cov,1)
    mulGau = normalize(mulGau)
    #uniform distribution[-1, 1]
    uniFor = np.random.uniform(-1.0,1.0, (1,N))
    uniFor = normalize(uniFor)

    tmpwChoice = np.random.randint(0,2)
    if(tmpwChoice == 0):
        wVec = mulGau
    else:
        wVec = uniFor
    variance = math.pow(10.0,np.random.randint(-4,5))

    #privacy compensation based on tanh
    pcVec = np.zeros(N, float)
    for i in range(N):
        pcVec[i] = math.tanh(abs(wVec[0,i]) * 1.0 /math.sqrt(variance))
    maxPc = max(pcVec)
    minPc = min(pcVec)
    intervalPc = (maxPc - minPc) * 1.0 / n
    for i in range(N):
        index = int((pcVec[i] - minPc) * 1.0 /intervalPc) - 1
        index = max(0, index)
        index = min(n - 1, index)
        xt[index, 0] = xt[index, 0] + pcVec[i]
        
    #must assign values
    xt = normalize(xt,'l2', axis=0)
    if printx == True:
        print('Finished! user_number is %d, feature vector dim is %d\n'%(N, n))
    return xt


def Query_feature_vector_v4(N, n, contribution, printx, alpha):
    #在最后的l2-norm之后加入贡献度
    if printx == True:
        print("gen v4 feature vectors")
        print('user_number is %d, feature vector dim is %d\n, alpha is %f'%(N, n, alpha))
    #final feature vctor
    xt = np.zeros((n,1),float)
    #N: the original number of data owners
    #N = 200
    

    #generate "weight vectors" in linear queries
    #multivariate Gaussian distribution (0, I)
    mg_mean = np.zeros(N,float)
    mg_cov = np.identity(N)
    mulGau = np.random.multivariate_normal(mg_mean,mg_cov,1)
    mulGau = normalize(mulGau)
    #uniform distribution[-1, 1]
    uniFor = np.random.uniform(-1.0,1.0, (1,N))
    uniFor = normalize(uniFor)

    tmpwChoice = np.random.randint(0,2)
    if(tmpwChoice == 0):
        wVec = mulGau
    else:
        wVec = uniFor
    variance = math.pow(10.0,np.random.randint(-4,5))

    #privacy compensation based on tanh
    pcVec = np.zeros(N, float)
    for i in range(N):
        pcVec[i] = math.tanh(abs(wVec[0,i]) * 1.0 /math.sqrt(variance))
    maxPc = max(pcVec)
    minPc = min(pcVec)
    intervalPc = (maxPc - minPc) * 1.0 / n
    for i in range(N):
        index = int((pcVec[i] - minPc) * 1.0 /intervalPc) - 1
        index = max(0, index)
        index = min(n - 1, index)
        xt[index, 0] = xt[index, 0] + pcVec[i]
        
    
    
    contribution_index = np.random.randint(0, len(contribution))
    contribution_vec = alpha * contribution[contribution_index] * np.ones((n,1),float)
    
    #must assign values
    xt = normalize(xt,'l2', axis=0)
    xt = xt + contribution_vec
    xt = normalize(xt,'l2', axis=0)
    if printx == True:
        print('Finished!')
    return xt



def self_normalize(theta,n,R2):
    tmp2sum = 0.0
    for i in range(n):
        tmp2sum += theta[i,0]**2
    for i in range(n):
        theta[i,0] = math.sqrt(theta[i,0]**2 * 1.0 /tmp2sum * R2)
    return theta


def Query_market_value_thetastar(n, R2):
    #thetaStar = np.zeros((n,1), float)

    # generate "weight vectors" in linear queries
    # multivariate Gaussian distribution (0, I)
    mg_mean = np.zeros(n, float)
    mg_cov = np.identity(n)
    mulGau = np.random.multivariate_normal(mg_mean, mg_cov, 1)
    mulGau = normalize(mulGau)
    # uniform distribution[-1, 1]
    uniFor = np.random.uniform(-1.0, 1.0, (1, n))
    uniFor = normalize(uniFor)

    tmpChoice = np.random.randint(0,2)
    if (tmpChoice == 0):
        thetaStar = abs(mulGau.transpose())
    else:
        thetaStar = abs(uniFor.transpose())
    thetaStar = self_normalize(thetaStar, n, R2)
    return thetaStar




if __name__=="__main__":
    contribution = [0.187, 0.1838, 0.1599, 0.1356, 0.0846, 0.0676, 0.0657, 0.0592, 0.0564,]
    
    
    #[0.215, 0.205, 0.112, 0.055, 0.043, 0.042, 0.038, 0.036, 0.036, 0.035, 0.034, 0.033, 0.033, 0.030, 0.030, 0.024]
    
    #part1: n = 100 隐私补偿 l2-norm
    #number of rounds
    T = 100000
    #number of features
    n = 100
    #2-norm domain of feature vector
    R2 = 4 * n
    #2-norm domain of weight vector
    S = 1
    
    #the true weight vector in market value
    thetaStar = Query_market_value_thetastar(n, R2/2.0)
    
    
    for N in [200]:
        X = np.zeros((T, n), float)
    
        for t in range(T):
            if t%10000 == 0:
                printx = True
            else:
                printx = False
            #Query Q_t
            #the feature vector xt
            xt = Query_feature_vector_v1(N, n, printx)
            xt_T = xt.transpose()
            X[t] = xt_T
            
         
        os.makedirs('./%dusers_%ddims_v1/'%(N, n),exist_ok=True)  
        os.makedirs('./%dusers_%ddims_v1/new_query/'%(N, n),exist_ok=True)  
        
        
        np.savetxt("./%dusers_%ddims_v1/new_query/X_T_%d_n_%d"%(N, n, T, n), X, fmt='%.10f')
        np.savetxt("./%dusers_%ddims_v1/new_query/theta_T_%d_n_%d"%(N, n, T, n), thetaStar.transpose(), fmt='%.10f')
    
    
    
    #part4: n = 100 隐私补偿 l2-norm + 贡献度 l2norm
    thetaStar = Query_market_value_thetastar(n, R2/2.0)
    
    for N in [200]:
        for alpha in [0.01, 0.1, 0.5, 1.0, 1.5, 2.0]:
            X = np.zeros((T, n), float)
        
            for t in range(T):
                if t%10000 == 0:
                    printx = True
                else:
                    printx = False
                #Query Q_t
                #the feature vector xt
                xt = Query_feature_vector_v4(N, n, contribution, printx, alpha)
                xt_T = xt.transpose()
                X[t] = xt_T
                
            
            os.makedirs('./%dusers_%ddims_v4_%falpha/'%(N, n, alpha),exist_ok=True)  
            os.makedirs('./%dusers_%ddims_v4_%falpha/new_query/'%(N, n, alpha),exist_ok=True)  
            
            
            np.savetxt("./%dusers_%ddims_v4_%falpha/new_query/X_T_%d_n_%d"%(N, n, alpha, T, n), X, fmt='%.10f')
            np.savetxt("./%dusers_%ddims_v4_%falpha/new_query/theta_T_%d_n_%d"%(N, n, alpha, T, n), thetaStar.transpose(), fmt='%.10f')
        