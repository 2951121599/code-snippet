# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  48_列表展开.py
# 日期时间：2022/5/7，18:30
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


print(spread([1, 2, 3, [4, 5, 6], [7], 8, 9]))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
