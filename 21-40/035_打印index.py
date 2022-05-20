# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  035_打印index.py
# 日期时间：2022/4/15，13:51
li = ['a', 'b', 'c', 'd']
for idx, item in enumerate(li):
    print(idx, '-->', item)

# 对两个序列进行计算或者处理
names = ['张三', '李四', '王五', '赵六']
colors = ['red', 'green', 'blue', 'yellow']
for name, color in zip(names, colors):
    print(name, '-->', color)
