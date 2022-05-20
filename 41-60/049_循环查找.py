# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  037_循环查找.py
# 日期时间：2022/4/15，14:07
target = 'd'
li = ['a', 'b', 'c']

for i in li:
    if i == target:
        print("找到")
        break
    # 打印三遍
    else:
        print("循环里未找到")
# 打印一遍
else:
    print("未找到")
