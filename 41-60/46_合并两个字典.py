# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  46_合并两个字典.py
# 日期时间：2022/5/7，18:22
def merge_two_dicts(a, b):
    c = a.copy()  # make a copy of a
    c.update(b)  # modify keys and values of a with the ones from b
    return c


a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
print(merge_two_dicts(a, b))  # {'x': 1, 'y': 3, 'z': 4}


# 方法2
def merge_dictionaries(a, b):
    return {**a, **b}


a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
print(merge_dictionaries(a, b))  # {'x': 1, 'y': 3, 'z': 4}
