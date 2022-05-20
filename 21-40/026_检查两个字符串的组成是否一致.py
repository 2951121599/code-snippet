# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  026_检查两个字符串的组成是否一致.py
# 日期时间：2022/4/2，16:43
from collections import Counter

str1 = 'hello'
str2 = 'elolh'
print(Counter(str1) == Counter(str2))
