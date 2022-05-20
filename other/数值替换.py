# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  数值替换.py
# 日期时间：2022/4/24，15:03
# 过滤出来的“负值”替换为“NaN”或者指定的值
import pandas as pd

df = pd.read_csv('tube.csv')
# A_H2O,A_CN,B_H2O,B_CN,C_H2O,C_CN,D_H2O,D_CN,E_H2O,E_CN,F_H2O,F_CN,G_H2O,G_CN
# 把大于或者小于100的值替换为0和1
df["A_H2O"][df.A_H2O < 1000] = 0
df["A_H2O"][df.A_H2O > 1000] = 1
df["A_CN"][df.A_CN < 1000] = 0
df["A_CN"][df.A_CN > 1000] = 1

df["B_H2O"][df.B_H2O < 1000] = 0
df["B_H2O"][df.B_H2O > 1000] = 1
df["B_CN"][df.B_CN < 1000] = 0
df["B_CN"][df.B_CN > 1000] = 1

df["C_H2O"][df.C_H2O < 1000] = 0
df["C_H2O"][df.C_H2O > 1000] = 1
df["C_CN"][df.C_CN < 1000] = 0
df["C_CN"][df.C_CN > 1000] = 1

df["D_H2O"][df.D_H2O < 1000] = 0
df["D_H2O"][df.D_H2O > 1000] = 1
df["D_CN"][df.D_CN < 1000] = 0
df["D_CN"][df.D_CN > 1000] = 1

df["E_H2O"][df.E_H2O < 1000] = 0
df["E_H2O"][df.E_H2O > 1000] = 1
df["E_CN"][df.E_CN < 1000] = 0
df["E_CN"][df.E_CN > 1000] = 1

df["F_H2O"][df.F_H2O < 1000] = 0
df["F_H2O"][df.F_H2O > 1000] = 1
df["F_CN"][df.F_CN < 1000] = 0
df["F_CN"][df.F_CN > 1000] = 1

df["G_H2O"][df.G_H2O < 1000] = 0
df["G_H2O"][df.G_H2O > 1000] = 1
df["G_CN"][df.G_CN < 1000] = 0
df["G_CN"][df.G_CN > 1000] = 1

df.to_csv('tube_result.csv', index=False)  # index = True/False 表示是否把索引index一起写入csv文本。
