# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  45_检查两个列表是不是有重复项.py
# 日期时间：2022/5/7，18:21
def has_duplicates(lst):
    return len(lst) != len(set(lst))


x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]
print(has_duplicates(x))  # True
print(has_duplicates(y))  # False
