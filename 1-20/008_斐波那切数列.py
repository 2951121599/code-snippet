# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  008_斐波那切数列.py
# 日期时间：2022/3/7，15:34
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    n = fibonacci(n - 2) + fibonacci(n - 1)
    return n


print(fibonacci(15))
