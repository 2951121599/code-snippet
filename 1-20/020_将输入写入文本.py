# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  020_将输入写入文本.py
# 日期时间：2022/3/7，15:52
# print("请输入3个数:")
# n = 3
# li = []
# while(n):
#     li.append(int(input("")))
#     n -= 1
li = [1, 2, 45, 49, 3]
# print(li)
strs = ""
for i in li:
    if (i % 3 == 0) or (i % 7 == 0):
        str_i = str(i) + " "
        strs += str_i
    else:
        pass

with open("record.txt", "w") as f:
    f.write(strs)
