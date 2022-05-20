# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  015_倒序删除列表元素.py
# 日期时间：2022/3/7，15:46
"""
删除元素原理:后一个元素覆盖前一个元素
解决方法:倒序删除元素
"""
# 方法1
list_num = [4, 5, 6, 4, 8, 9]
for i in range(len(list_num) - 1, -1, -1):
    if list_num[i] % 2 == 0:
        # 删除的是列表元素 而不是 i 索引
        del list_num[i]
print(list_num)

# 方法2
list_num = [4, 5, 6, 4, 8, 9]
for i in range(len(list_num) - 1, -1, -1):
    if list_num[i] % 2 == 0:
        list_num.remove(list_num[i])
print(list_num)

# 不会删除元素 直接把符合要求的添加到新列表
list_num = [4, 5, 6, 4, 8, 9]
new_list = []
for i in list_num:
    if i % 2 != 0:
        new_list.append(i)
print(new_list)
