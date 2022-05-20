# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  002_装饰器函数-计算函数运行时间时间.py
# 日期时间：2022/3/7，15:30
import time


def calc_func_runtime(func):
    """
        装饰器函数, 计算函数运行时间时间
    :param func: 需要计算的函数
    :return: 运行时间
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print("%s函数运行时间：%.6f" % (func.__name__, end_time - start_time))
        return res

    return wrapper
