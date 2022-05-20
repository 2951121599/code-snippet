# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  021_列表中出现最频繁的数.py
# 日期时间：2022/3/7，15:55
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1]
print(max(set(test), key=test.count))
# from collections import Counter
#
# print((Counter(test)).most_common(1)[0][0])
