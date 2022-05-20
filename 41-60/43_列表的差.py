# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  43_列表的差.py
# 日期时间：2022/5/7，18:14
"""
该方法将返回第一个列表的元素，其不在第二个列表内。
如果同时要反馈第二个列表独有的元素，还需要加一句 set_b.difference(set_a)
"""


def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)


print(difference([1, 2, 3], [1, 2, 4]))  # [3]


def difference_by(a, b, fn):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]


from math import floor

print(difference_by([2.1, 1.2], [2.3, 3.4], floor))  # [1.2]
