# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  038_切割列表.py
# 日期时间：2022/5/7，18:00
"""
给定具体的大小，定义一个函数以按照这个大小切割列表
"""
from math import ceil


def chunk(lst, size):
    return list(
        map(lambda x: lst[x * size:x * size + size], list(range(0, ceil(len(lst) / size))))
    )


li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(chunk(li, 2))  # [[1, 2], [3, 4], [5, 6], [7, 8], [9]]
print(chunk(li, 3))  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
