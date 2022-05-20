# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  032_字典合并.py
# 日期时间：2022/4/6，18:26
d1 = {'a': 1}
d2 = {'b': 2}
# 三种方式
print({**d1, **d2})  # {'a': 1, 'b': 2}
print(dict(d1.items() | d2.items()))  # {'a': 1, 'b': 2}
d1.update(d2)
print(d1)  # {'a': 1, 'b': 2}
