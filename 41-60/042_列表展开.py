# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  42_列表展开.py
# 日期时间：2022/5/7，18:12
"""
通过递归的方式将列表的嵌套展开为单个列表
"""


def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


def deep_flatten(lst):
    result = []
    result.extend(
        spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))
    return result


print(deep_flatten([1, [2], [[3], 4], 5]))  # [1, 2, 3, 4, 5]
