# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  007_求阶乘.py
# 日期时间：2022/3/7，15:34
def factorial(n):
    if n == 1:
        return n  # 阶乘为1的时候，结果为1,返回结果并退出
    n = n * factorial(n - 1)  # n! = n*(n-1)!
    return n  # 返回结果并退出


res = factorial(5)
print(res)
