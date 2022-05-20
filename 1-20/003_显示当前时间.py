# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  003_显示当前时间.py
# 日期时间：2022/3/7，15:31
import time

str_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(str_datetime)
