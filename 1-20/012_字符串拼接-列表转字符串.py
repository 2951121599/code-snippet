# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  012_字符串拼接-列表转字符串.py
# 日期时间：2022/3/7，15:44
"""
0123456789
"""
# 避免产生过多的无用字符串
# 用可变对象替代不可变对象
# 面试不要你  一定不要用
str_result = ""
for i in range(10):
    # 两个字符串拼接 产生新的字符串对象
    str_result += str(i)
print(str_result)

list_result = []
for i in range(10):
    # 两个字符串拼接 产生新的字符串对象
    list_result.append(str(i))
str_result2 = "".join(list_result)
print(str_result2)

# 列表转换字符串
# result = "连接符".join(列表)
