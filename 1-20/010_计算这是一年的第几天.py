# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  010_计算这是一年的第几天.py
# 日期时间：2022/3/7，15:38
"""
输入年月日 计算这是一年的第几天
2019年3月5日
31 + 28 + 5
"""
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入天："))
if month < 0 or month > 12:
    print("月份输入错误！")
if day < 0 or day > 31:
    print("天数输入错误！")
else:
    # 计算2月的天数
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        d = 29
    else:
        d = 28
    # 元组存储
    day_of_month = (31, d, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    total_day = 0
    for i in range(month - 1):
        total_day += day_of_month[i]
    # 利用切片 和 内置函数
    total_day2 = sum(day_of_month[:month - 1])
    print(total_day + day)
    print(total_day2 + day)
