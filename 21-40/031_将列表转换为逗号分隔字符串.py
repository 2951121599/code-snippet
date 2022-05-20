# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  031_将列表转换为逗号分隔字符串.py
# 日期时间：2022/4/6，18:22
li = ['a', 'b', 'c']
print(','.join(li))  # a,b,c

numbers = [1, 2, 3, 4, 5]
print(','.join(map(str, numbers)))  # 1,2,3,4,5

data = [2, 'hello', 3, 3.4]
print(','.join(map(str, data)))  # 2,hello,3,3.4
