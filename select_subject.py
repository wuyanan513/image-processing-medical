
import os
from tqdm import trange
import pandas as pd


def get_ct_file(main_path):
    ctpath = []
    ct_list = os.listdir(main_path)  # 列出文件夹下所有的目录与文件
    # 遍历该文件夹下的所有目录或者文件
    for ii in range(0, len(ct_list)):
        path = os.path.join(main_path, ct_list[ii])
        ctpath.append(path)
    return ctpath


if __name__ == '__main__':

    # 原始数据，不能有中文
    main_path = r'H:\AZ\FC03'
    save_path = r'E:\1-paper\3-MIP-classification\data'

    ct_path = get_ct_file(main_path)
    ct_path.sort()
    ct_name = []
    ct_date = []
    for i in trange(len(ct_path)):
        ct_name_path = ct_path[i].split('_')[0]
        ct_name.append(os.path.split(ct_name_path)[1])
        ct_date.append(ct_path[i].split('_')[1])
    data2 = {'ct_name': ct_name, 'ct_date': ct_date}  # , 'predict': test_save_output,'score':score_new_test, }
    df2 = pd.DataFrame(data2)
    df2.to_csv(os.path.join(save_path, 'Pulmonary Function.csv'), index=None)
    print('Finished saving csvfile!')