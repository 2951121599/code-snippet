# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  check_tool_to_excel.py
# 日期时间：2021/8/13，09:44
import os
import sys
import pandas as pd
import configparser
from pathlib import Path
from tkinter import messagebox, Tk

config = configparser.ConfigParser()
config.read('config.ini')
batch = config['batch_info']['batch']

# 相关路径
root_path = Path.cwd()

# ion_list = ['pos']
ion_list = ['neg', 'pos']


# 窗口显示错误信息
def show_error(root, error_info):
    root.withdraw()  # 实现主窗口隐藏
    messagebox.showerror("错误信息", error_info)  # 显示错误
    sys.exit()  # 程序退出


# 计算SST样本面积的RSD
def calc_sst_area_rsd(df):
    feature = df.iloc[:, 0]
    # 过滤SST数据
    sst_df = df.filter(regex="_SST_")
    sst_df = sst_df.iloc[:, -6:]
    print("后6个SST", sst_df.columns.tolist())
    # 计算rsd 标准差/均值*100
    rsd = round(sst_df.std(axis=1) / sst_df.mean(axis=1) * 100, 2).to_frame(name='SST_RSD')

    sst_df = pd.concat([feature, sst_df], axis=1)
    result = pd.concat([sst_df, rsd], axis=1)
    result['check_result'] = result['SST_RSD'].apply(lambda x: 1 if x <= 15 else 0)  # 根据条件添加一列
    result = result.sort_values(by=['SST_RSD'], ascending=False, na_position='first')  # 降序
    return result


# 计算QC样本面积的RSD
def calc_qc_area_rsd(df):
    feature = df.iloc[:, 0]
    # 过滤QC数据
    qc_df = df.filter(regex="_QC_")
    # 计算rsd 标准差/均值*100
    rsd = round(qc_df.std(axis=1) / qc_df.mean(axis=1) * 100, 2)

    rsd = rsd.to_frame(name='QC_RSD')  # 将Series转为DataFrame
    qc_df = pd.concat([feature, qc_df], axis=1)
    result = pd.concat([qc_df, rsd], axis=1)
    result['check_result'] = result['QC_RSD'].apply(lambda x: 1 if x <= 15 else 0)  # 根据条件添加一列
    result = result.sort_values(by=['QC_RSD'], ascending=False, na_position='first')  # 降序
    return result


# 计算QC样本峰高的RSD
def calc_qc_peak_height_rsd(df):
    feature_list = df.loc[:, 'ion_code'].drop_duplicates()
    qc_sample_list = df[df['sample_number'].str.contains('_QC_')]['sample_number'].drop_duplicates().tolist()

    res_rsd = None
    df_qc_peak_height = None

    for feature in feature_list:
        each_feature_qc_df = df[(df['sample_number'].str.contains('_QC_')) & (df['ion_code'] == feature)][
            'rt_peak_height'].to_frame(name=feature)
        each_feature_qc_df.index = qc_sample_list

        # 计算rsd 标准差/均值*100
        each_rsd = round(each_feature_qc_df.std(axis=0) / each_feature_qc_df.mean(axis=0) * 100, 2).to_frame(
            'QC_peak_height_RSD')
        df_qc_peak_height = pd.concat([df_qc_peak_height, each_feature_qc_df], axis=1)
        res_rsd = pd.concat([res_rsd, each_rsd], axis=0)
    result = pd.concat([df_qc_peak_height.T, res_rsd], axis=1)
    result['check_result'] = result['QC_peak_height_RSD'].apply(lambda x: 1 if x <= 15 else 0)  # 根据条件添加一列
    result = result.sort_values(by=['QC_peak_height_RSD'], ascending=False, na_position='first')  # 降序
    return result


# 计算QC样本RT的RSD
def calc_qc_rt_rsd(df):
    feature_list = df.loc[:, 'ion_code'].drop_duplicates()
    qc_sample_list = df[df['sample_number'].str.contains('_QC_')]['sample_number'].drop_duplicates().tolist()

    res_std = None
    res_mean = None
    res_range = None
    df_qc_rt = None

    for feature in feature_list:
        each_feature_qc_df = df[(df['sample_number'].str.contains('_QC_')) & (df['ion_code'] == feature)][
            'new_rt'].to_frame(name=feature)
        each_feature_qc_df.index = qc_sample_list

        # 计算均值, 标准差, 极值
        each_mean = round(each_feature_qc_df.mean(axis=0), 2).to_frame('mean')
        each_std = round(each_feature_qc_df.std(axis=0), 3).to_frame('std')
        each_range = round(each_feature_qc_df.max(axis=0) - each_feature_qc_df.min(axis=0), 3).to_frame('range')
        df_qc_rt = pd.concat([df_qc_rt, each_feature_qc_df], axis=1)
        res_std = pd.concat([res_std, each_std], axis=0)
        res_mean = pd.concat([res_mean, each_mean], axis=0)
        res_range = pd.concat([res_range, each_range], axis=0)
    tmp_1 = pd.concat([df_qc_rt.T, res_mean], axis=1)
    tmp_2 = pd.concat([tmp_1, res_std], axis=1)
    result = pd.concat([tmp_2, res_range], axis=1)
    result['check_std'] = result['std'].apply(lambda x: 1 if x < 0.015 else 0)  # 根据条件添加一列 标准差大于等于0.015的标记为0
    result['check_range'] = result['range'].apply(lambda x: 1 if x < 0.05 else 0)  # 根据条件添加一列 极差大于等于0.05的标记为0
    result = result.sort_values(by=['range'], ascending=False, na_position='first')  # 降序
    return result


root = Tk()  # 初始化报错信息窗口对象
# 计算结果存入Excel
for ion in ion_list:
    file_root_path = root_path.joinpath(batch, ion)
    df_area_merge = ""
    df_draw_info = ""
    try:
        area_merge_file_path = \
            [file_root_path.joinpath(i) for i in os.listdir(file_root_path) if i.endswith(ion + '_area_merge.csv')][0]
        df_area_merge = pd.read_csv(area_merge_file_path)
    except Exception as e:
        show_error(root, "%s_area_merge.csv文件不存在 !!!\n%s" % (ion, e))

    try:
        draw_info_file_path = \
            [file_root_path.joinpath(i) for i in os.listdir(file_root_path) if
             i.endswith(ion + '_draw_info_merge.csv')][0]
        df_draw_info = pd.read_csv(draw_info_file_path)
    except Exception as e:
        show_error(root, "%s_draw_info_merge.csv文件不存在 !!!\n%s" % (ion, e))

    # 计算SST样本面积的RSD
    res_sst_area_rsd = calc_sst_area_rsd(df_area_merge)

    # 计算QC样本面积的RSD
    res_qc_area_rsd = calc_qc_area_rsd(df_area_merge)

    # 计算QC样本峰高的RSD
    res_qc_peak_height_rsd = calc_qc_peak_height_rsd(df_draw_info)

    # 计算QC样本RT的mean, std, range
    res_qc_rt_rsd = calc_qc_rt_rsd(df_draw_info)

    # 输出文件
    output_excel = os.path.join(file_root_path, ion + '_check_result.xlsx')
    if os.path.exists(output_excel):
        os.remove(output_excel)
    with pd.ExcelWriter(output_excel) as writer:
        res_sst_area_rsd.to_excel(writer, sheet_name=ion + "_SST样本面积的RSD", index=False)
        res_qc_area_rsd.to_excel(writer, sheet_name=ion + "_QC样本面积的RSD", index=False)
        res_qc_peak_height_rsd.to_excel(writer, sheet_name=ion + "_QC样本峰高的RSD", index_label="feature")
        res_qc_rt_rsd.to_excel(writer, sheet_name=ion + "_QC样本RT的mean&std&range", index_label="feature")
    print(ion + '_check_result.xlsx' + " 生成成功! ")
