# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  001_判断一个数是否为质数.py
# 日期时间：2022/3/7，15:29
import math


def is_prime(n):
    """
        判断一个数是否为质数
    :param n: 判断的数据
    :return: bool
    """
    if n <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


for i in range(20):
    if is_prime(i):
        print(i)
