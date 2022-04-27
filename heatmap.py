
import numpy as np #导入numpy计算包，没装包的需要先安装下
import seaborn as sns #导入画图包
import matplotlib.pyplot as plt

corr_mat = [[0.0474,0.0487,0.051,0.0529,0.0535],
[0.0533,0.0522,0.0511,0.0502,0.0495],
[0.0489,0.0482,0.047,0.046,0.0448],[0.0437,0.0445,0.0473,0.0554,0.0639]]
# print(corr_mat)[[0,0.1934,0.5388,0.365,0.2155,0.0878,0.4271],
# [0,0,0.2131,0.0573,0.2567,0.1499,0.1315],
# [0,0,0,0.3093,0.4902,0.3287,0.0001],[0,0,0,0,0.3757,0.2966,0.0001],
# [0,0,0,0,0,0.316,0.0001],[0,0,0,0,0,0,0.0004],[0,0,0,0,0,0,0]]
num_classes = 5
labels = []
# f, ax = plt.subplots(figsize=(12, 8)) #定义画布的大小

mask = np.zeros_like(corr_mat)
# print(range(num_classes))
# for i in range(0,len(mask)):
#     for j in range(0,i+1):
#         mask[i][j] = True# 掩盖掉上面的三角形

ax = sns.heatmap(corr_mat, annot=True,mask=mask,linewidths=.05,square=True,annot_kws={'size':10})#显示相关性数值
plt.rcParams['font.sans-serif'] = 'Times New Roman'
plt.xticks(range(num_classes),labels,rotation=45,fontsize=12
                 )# rotation=45,,fontsize=12
# 设置y轴坐标label
plt.yticks(range(num_classes),labels,rotation=45,fontsize=12)# rotation=45,,fontsize=12

# plt.xlabel(rotation=45)
# plt.ylabel(rotation=45)
# 显示colorbar
# plt.colorbar()
# plt.xlabel('True Labels',fontsize=14)
# plt.ylabel('Predicted Labels',fontsize=14)
plt.title('P Value',fontsize=12)

plt.subplots_adjust(left=.1, right=0.95, bottom=0.22, top=0.95)#设置画布边缘尺寸，可以自己调整
plt.savefig('相关性.png',dpi=600)#设置图片地址这里是相对地址，图片保存为矢量图分辨率300，

plt.show()#显示绘图内容