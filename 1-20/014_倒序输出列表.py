# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  014_倒序输出列表.py
# 日期时间：2022/3/7，15:45
list_name = []
while True:
    str_name = input("请输入你喜欢的人名:")
    if str_name == "":
        break
    if str_name not in list_name:
        list_name.append(str_name)
    else:
        print("名称已经存在,不在录入")
for i in list_name[::-1]:
    print(i)

# #  通过切片访问列表元素(浅拷贝 费内存)
# for i in list_name[::-1]:
#     print(i)
# #  通过索引访问列表元素(推荐)
# for i in range(len(list_name)-1, -1, - 1):
#     print(list_name[i])
