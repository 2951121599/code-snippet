# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  判断操作系统及架构信息.py
# 日期时间：2022/3/17，15:40

# 三种操作系统 uos ky centos
# 两种架构: x86和arm
import sys
import platform

os_list = ['uos', 'ky', 'centos', 'Windows']
architecture_list = ['x86', 'arm', 'WindowsPE']
os_name = platform.system()
architecture_name = platform.architecture()[1]


# print(architecture_name)
# print(platform.architecture())  # ('64bit', 'WindowsPE')
# print(sys.platform)  # win32


# 判断是哪个架构
def which_architecture(architecture_name):
    if architecture_name == architecture_list[0]:  # x86
        print(architecture_name)
    elif architecture_name == architecture_list[1]:  # arm
        print(architecture_name)
    else:  # WindowsPE或其它
        print(architecture_name)


# 判断是否是列表中的os
if os_name in os_list:
    print(os_name)
    if os_name == os_list[0]:  # uos
        which_architecture(architecture_name)
    elif os_name == os_list[1]:  # ky
        which_architecture(architecture_name)
    elif os_name == os_list[2]:  # centos
        which_architecture(architecture_name)
    else:  # Windows或其它
        which_architecture(architecture_name)
else:
    print('其他系统')
