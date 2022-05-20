# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  017_判断闰年.py
# 日期时间：2022/3/7，15:48
"""
根据输入的年份 月份 输出对应的天数
"""
year = int(input("请输入年份："))
month = int(input("请输入月份："))
if month < 0 or month > 12:
    print("月份输入错误！")
else:
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("29天")
        else:
            print("28天")
    else:
        print("31天")
