# -*-coding:utf-8-*- 
# ���ߣ�   29511
# �ļ���:  �����κ����Ľ׳�.py
# ����ʱ�䣺2021/7/28��11:19
import functools

result = (lambda k: functools.reduce(int.__mul__, range(1, k + 1), 1))(5)

print(result)
