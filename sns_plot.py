import xlrd
import seaborn as sns
from pandas.core.frame import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#
# def xls_read(xls_path):
#     folder_name,number,RU_em,RM_em,RL_em,R_em,LU_em,LL_em,L_em,all_em=[],[],[],[],[],[],[],[],[],[]
#     # read_book=xlrd.open_workbook(xls_path)
#     # # table = read_book.sheet_by_name('e\x00m\x00p\x00h\x00y\x00s\x00e\x00m\x00a\x00')
#     # table=read_book.sheet_by_index(0)
#     # nrows=table.nrows
#     data=pd.read_excel(xls_path)
#     # read value and save
#     for i in range(1,nrows):
#         folder_name.append(table.cell_value(i,0))
#         number.append(float(table.cell_value(i,1)))
#         RU_em.append(float(table.cell_value(i,2)))
#         RM_em.append(float(table.cell_value(i,3)))
#         RL_em.append(float(table.cell_value(i,4)))
#         R_em.append(float(table.cell_value(i,5)))
#         LU_em.append(float(table.cell_value(i,6)))
#         LL_em.append(float(table.cell_value(i,7)))
#         L_em.append(float(table.cell_value(i,8)))
#         all_em.append(float(table.cell_value(i,9)))
#
#     return  folder_name,number,RU_em,RM_em,RL_em,R_em,LU_em,LL_em,L_em,all_em
#


if __name__ == '__main__':
    # location = ['1','2','3','R','LU','LL','L','lung']
    category = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                '12', '13', '14', '15', '16', '17', '18', '19', '20']
    xls_path='attention_HC.xls'
    data = pd.read_excel(xls_path)
    # print(data)
    # em_data = data.iloc[:,2:10]
    # print(em_data)
    # folder_name,number,RU_em,RM_em,RL_em,R_em,LU_em,LL_em,L_em,all_em = xls_read(xls_path)
    # em = {'RU_em': RU_em,'RM_em':RM_em,'RL_em':RL_em,'R_em','LU_em','LL_em','L_em','all_em'}
    # em = np.array(em)

    # plt.figure(figsize=(20, 10))
    sns.set(style="ticks")
    # plt.figure(figsize=(8, 6))

    # exercise = sns.load_dataset("exercise")
    g = sns.catplot(data=data, kind = "bar",height=5,aspect=1.5, palette = "deep")
    plt.ylabel('Mean±SD',font= 'Times New Romance', labelpad=2)
    plt.xlabel('Instances',font= 'Times New Romance', labelpad=2)
    plt.savefig('attention_weight_HC.png', dpi=600)
    plt.show()
    #

    # plt.show()
    # titanic = sns.load_dataset("titanic")
    # sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic)
    # plt.show()
    