# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  018_时间转换.py
# 日期时间：2022/3/7，15:48
"""
在控制台中录入一个秒，计算是几小时零几分钟零几秒钟
"""
total_second = int(input("请输入总秒数:"))
hour = total_second // 3600
minute = total_second // 60 % 60
second = total_second % 60
print("%d秒是" % total_second + str(hour) + "小时" + str(minute) + "分" + str(second) + "秒")