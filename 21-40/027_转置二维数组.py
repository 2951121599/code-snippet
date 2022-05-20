# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  027_转置二维数组.py
# 日期时间：2022/4/2，16:50
from itertools import chain

original = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(original)
transposed = zip(*original)
print(list(transposed))  # [('a', 'c', 'e'), ('b', 'd', 'f')]

# 二维转一维
print(list(chain.from_iterable(original)))  # ['a', 'b', 'c', 'd', 'e', 'f']
