# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  040_成对列表解开.py
# 日期时间：2022/5/7，18:06
"""
可以将打包好的成对列表解开成两组不同的元组
"""
array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*array)
for i in transposed:  # [('a', 'c', 'e'), ('b', 'd', 'f')]
    print(i)
