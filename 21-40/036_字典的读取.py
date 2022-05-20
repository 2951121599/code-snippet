# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  036_字典的读取.py
# 日期时间：2022/4/15，14:01
students = {
    '张三': 20,
    '李四': 22
}

stu = students.get('张三', '未找到')
print("张三 {} 岁了".format(stu))

# 利用字典get的缺省值,避免找不到keys时报错
stu = students.get('王五', '未找到')
print("王五 {} 岁了".format(stu))
