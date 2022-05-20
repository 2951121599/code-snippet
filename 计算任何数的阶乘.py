# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  计算任何数的阶乘.py
# 日期时间：2021/7/28，11:19
import functools

result = (lambda k: functools.reduce(int.__mul__, range(1, k + 1), 1))(5)

print(result)
