# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  006_求最大公约数.py
# 日期时间：2022/3/7，15:33
def gcd(x, y):
    while y:
        t = x % y
        x = y
        y = t
    return x


print(gcd(4, 24))
