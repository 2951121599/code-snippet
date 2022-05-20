# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  023_翻转数字字符串列表的方式.py
# 日期时间：2022/3/7，16:01
# 反转数字
test_num = 123456789
print(int(str(test_num)[::-1]))  # 987654321

# 反转字符串
test_str = "Test Python"
print(test_str[::-1])  # nohtyP tseT

# 反转列表
test_list = [1, 3, 5]
test_list.reverse()  # reverse()改变原始列表
print(test_list)  # [5, 3, 1]
print(test_list[::-1])  # [1, 3, 5]
