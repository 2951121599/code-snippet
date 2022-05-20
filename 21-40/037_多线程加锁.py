# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  037_多线程加锁.py
# 日期时间：2022/4/15，14:36
import threading

lock = threading.Lock()
with lock:
    print("加锁")
