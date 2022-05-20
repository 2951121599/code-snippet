# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  005_统计字符串中含有数字等的个数.py
# 日期时间：2022/3/7，15:32
def func(*param):
    length = len(param)
    for i in range(length):
        letters = 0
        space = 0
        number = 0
        other = 0
        for item in param[i]:
            if item.isalpha():
                letters += 1
            elif item == " ":
                space += 1
            elif item.isdigit():
                number += 1
            else:
                other += 1
        print(letters, space, number, other)


func("dfsfasfsfsaf  sfsfsafs35f5fd")
