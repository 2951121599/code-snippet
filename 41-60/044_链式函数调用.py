# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  44_链式函数调用.py
# 日期时间：2022/5/7，18:18
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


x, y = 4, 5
print((sub if x > y else add)(x, y))  # 9
