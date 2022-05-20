# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  004_组成多少个不重复的5位偶数.py
# 日期时间：2022/3/7，15:32
# "012345",可以组成多少个不重复的5位偶数 (312个)
import itertools

str_num = "012345"
for item in filter(lambda item: item[0] != "0" and int(item[-1]) % 2 == 0, itertools.permutations(str_num, 5)):
    # ('1', '0', '2', '3', '4') -->"10234" --> 10234
    print(int("".join(item)))

result = tuple(filter(lambda item: item[0] != "0" and int(item[-1]) % 2 == 0, itertools.permutations(str_num, 5)))
print(len(result))
