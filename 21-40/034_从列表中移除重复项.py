# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  034_从列表中移除重复项.py
# 日期时间：2022/4/7，10:07
li = [2, 2, 3, 3, 1]
print(list(set(li)))  # [1, 2, 3]

from collections import OrderedDict

print(list(OrderedDict.fromkeys(li).keys()))  # [2, 3, 1]
