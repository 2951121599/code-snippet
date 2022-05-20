# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  025_查询列表中出现频率最多的元素.py
# 日期时间：2022/4/2，16:38
from collections import Counter

li = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
print(max(set(li), key=li.count))

print(Counter(li).most_common(1))
print(Counter(li).most_common(1)[0][0])
