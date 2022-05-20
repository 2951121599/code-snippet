# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  039_将布尔型的值去掉.py
# 日期时间：2022/5/7，18:04
"""
例如(False, None, 0, "")，使用 filter() 函数
"""


def compact(lst):
    return list(filter(bool, lst))


print(compact([0, 1, 2, '', 3, 'a', 'b', 4, False, None]))  # [1, 2, 3, 'a', 'b', 4]
