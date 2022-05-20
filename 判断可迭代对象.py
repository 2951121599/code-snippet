# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  判断可迭代对象.py
# 日期时间：2022/1/28，16:24
from collections.abc import Iterable

# str list tuple dict set, range 可迭代对象
print(isinstance('abc', Iterable))  # True
print(isinstance('', Iterable))  # True
print(isinstance([], Iterable))  # True
print(isinstance((), Iterable))  # True
print(isinstance({}, Iterable))  # True
print(isinstance(set(), Iterable))  # True
print(isinstance(range(3), Iterable))  # True
