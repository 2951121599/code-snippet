# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  011_反转字符串.py
# 日期时间：2022/3/7，15:38
"""
拆分反转字符串
将英文语句，进行单词反转(结果还是str).
How are you --> you are How
"""
str_msg = "How are you"
list_temp = str_msg.split(" ")
str_result = " ".join(list_temp[::-1])
print(str_result)
