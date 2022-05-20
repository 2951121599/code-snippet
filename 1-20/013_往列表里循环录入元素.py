# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  013_往列表里循环录入元素.py
# 日期时间：2022/3/7，15:44
list_score = []
while True:
    score = input("请输入学生成绩:")
    if score == "":
        break
    score = int(score)
    list_score.append(score)
