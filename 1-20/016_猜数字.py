# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  016_猜数字.py
# 日期时间：2022/3/7，15:47
"""
在终端中重复猜测 知道猜中为止
提示猜大了 猜小了 猜中了
并输出一共猜了多少次
"""
import random

# 猜的次数
guess_count = 0
# 生成数字
number = random.randint(0, 100)
# 作弊
print(number)
while True:
    # 先加上次数,防止退出
    guess_count += 1
    user_number = int(input())
    if user_number == number:
        print("恭喜你猜中了，你一共猜了%d次" % guess_count)
        break
    elif user_number > number:
        print("太大了")
    else:
        print("太小了")
