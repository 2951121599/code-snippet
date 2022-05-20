# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  028_列表复制浅拷贝与深拷贝.py
# 日期时间：2022/4/2，17:33
from copy import copy, deepcopy

origin = [1, 2, [3, 4]]
# origin 里边有三个元素：1， 2，[3, 4]
cop1 = copy(origin)
cop2 = deepcopy(origin)
print(cop1)  # [1, 2, [3, 4]]
print(cop2)  # [1, 2, [3, 4]]
print(origin is cop1)  # False
print(origin is cop2)  # False
print(cop1 == cop2)  # True
print(cop1 is cop2)  # False
# cop1 和 cop2 看上去相同，但已不再是同一个object
origin[2][0] = 100
print(origin)  # [1, 2, [100, 4]]

print(cop1)  # [1, 2, [100, 4]]
print(cop2)  # [1, 2, [3, 4]]
