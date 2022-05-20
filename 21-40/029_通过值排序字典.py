# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  029_通过值排序字典.py
# 日期时间：2022/4/2，17:55
from operator import itemgetter

d = {
    'apple': 10,
    'orange': 20,
    'banana': 5,
    'tomato': 1
}
# 方式1:通过关键字key
print(sorted(d.items(), key=lambda x: x[1]))  # print(sorted(d.items(), key=itemgetter(1)))
# 方式2:通过关键字itemgetter
print(sorted(d.items(), key=itemgetter(1)))  # [('tomato', 1), ('banana', 5), ('apple', 10), ('orange', 20)]
# 方式3:通过value
print(sorted(d, key=d.get))  # ['tomato', 'banana', 'apple', 'orange']
