# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  47_将两个列表转化为字典.py
# 日期时间：2022/5/7，18:24
def to_dictionary(keys, values):
    return dict(zip(keys, values))


keys = ["a", "b", "c"]
values = [2, 3, 4]
print(to_dictionary(keys, values))  # {'a': 2, 'b': 3, 'c': 4}
