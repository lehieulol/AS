import numpy as np
import random

def DBScan(X, k=16, num_iterations=10):
    m, n = X.shape
    minPTs = 6
    epsilon_top = 1.73205080757
    epsilon_bot = 0
    epsilon = 0
    # Initialize parameters
    # np.random.random(X)
    
    ret_idx = np.zeros(m)

    while(num_iterations > 0):
        num_iterations-=1
        epsilon = (epsilon_bot+epsilon_top)/2

        # find core point
        is_core = np.zeros(m)
        
        for i in range(m):
            count = 0
            for j in range(m):
                if (np.linalg.norm(X[i] - X[j]) <= epsilon):
                    count+=1
            if count > minPTs:
                is_core[i] = 1

        # DFS
        idx = np.zeros(m)
        cnt = 1
        stack = []
        for i in range(m):
            if (idx[i] != 0):
                continue
            if (is_core[i] == 0):
                continue
            idx[i] = cnt
            cnt += 1
            stack.append(i)
            while(len(stack) > 0):
                top = stack.pop()
                for j in range(m):
                    if (top == j):
                        continue
                    if (np.linalg.norm(X[top] - X[j]) <= epsilon):
                        idx[j] = cnt
                        if (is_core[j] == 1):
                            stack.append(j)
        -
        if (cnt >= k):
            epsilon_top = epsilon
        else:
            epsilon_bot = epsilon
        ret_idx = idx
    
    centroid = np.zeros(shape=(k, n))
    cnt = np.zeros(shape=k)
    for i in range(m):
        centroid[ret_idx[i]]+=X[i]
        cnt[ret_idx[i]]+=1
    centroid = centroid/cnt
    return ret_idx, centroid
