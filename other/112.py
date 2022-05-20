# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  112.py
# 日期时间：2022/4/22，11:49
import os
from utilmy import oos

print(oos.os_cpu())
# os_makedirs('ztmp/ztmp2/myfile.txt')
import random


def log(*s):
    print(*s, flush=True)


def pd_random(ncols=7, nrows=100):
    import pandas as pd
    ll = [[random.random() for i in range(0, ncols)] for j in range(0, nrows)]
    df = pd.DataFrame(ll, columns=[str(i) for i in range(0, ncols)])
    return df


def pd_generate_data(ncols=7, nrows=100):
    """ Generate sample data for function testing
    categorical features for anova test
    """
    import numpy as np, pandas as pd
    np.random.seed(444)
    numerical = [[random.random() for i in range(0, ncols)] for j in range(0, nrows)]
    df = pd.DataFrame(numerical, columns=[str(i) for i in range(0, ncols)])
    df['cat1'] = np.random.choice(a=[0, 1], size=nrows, p=[0.7, 0.3])
    df['cat2'] = np.random.choice(a=[4, 5, 6], size=nrows, p=[0.5, 0.3, 0.2])
    df['cat1'] = np.where(df['cat1'] == 0, 'low', np.where(df['cat1'] == 1, 'High', 'V.High'))
    return df


log(1, 2, 'sadf')
log(11, 2, 'sadf')
log(111, 2, 'sadf')
