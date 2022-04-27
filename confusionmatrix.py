import numpy as np
import matplotlib.pyplot as plt


# plot Confusion matrix
num_classes = 2
labels = ['COPD','HC']
matrix = [[78,23],
 [11,89]]
matrix = np.array(matrix)
print(matrix)
plt.imshow(matrix, cmap=plt.cm.Blues)
plt.rcParams['font.sans-serif'] = 'Times New Roman'
# 设置x轴坐标label
plt.yticks(range(num_classes), labels,fontsize=14)
# 设置y轴坐标label
plt.xticks(range(num_classes), labels,rotation=45,fontsize=14)
# 显示colorbar
plt.colorbar()
plt.ylabel('True Labels',fontsize=14)
plt.xlabel('Predicted Labels',fontsize=14)
# plt.title('Confusion matrix',fontsize=14)

# 在图中标注数量/概率信息
thresh = matrix.max() / 2
for x in range(num_classes):
    for y in range(num_classes):
        # 注意这里的matrix[y, x]不是matrix[x, y]
        info = int(matrix[y, x])
        plt.text(x, y, info,
                 verticalalignment='center',
                 horizontalalignment='center',
                 color="white" if info > thresh else "black",fontsize=14)
plt.tight_layout()
plt.savefig("LR_dalian.png",dpi=600)
plt.show()
# num_classes = 4
# labels = ['CLE','PLE','PSE','NLP']
# plt.figure()
# plt.subplot(1,2,1)
# matrix = [[64,3,1,1], [6,62,2,4],[0,1,72,1],[2,7,0,95]]
# matrix = np.array(matrix)
# print(matrix)
# plt.imshow(matrix, cmap=plt.cm.Blues)
# plt.rcParams['font.sans-serif'] = 'Times New Roman'
# # plt.rcParams['figure.dpi'] = 600
# # 设置x轴坐标label
# plt.xticks(range(num_classes), labels, rotation=45,fontsize=14)
# # 设置y轴坐标label
# plt.yticks(range(num_classes), labels,fontsize=14)
# # 显示colorbar
# plt.colorbar(fraction=0.05, pad=0.05)
# plt.ylabel('True Labels',fontsize=14)
# plt.xlabel('Predicted Labels\n(a)',fontsize=14)
# plt.title('Confusion matrix',fontsize=14)
#
# # 在图中标注数量/概率信息
# thresh = matrix.max() / 2
# for x in range(num_classes):
#     for y in range(num_classes):
#         # 注意这里的matrix[y, x]不是matrix[x, y]
#         info = int(matrix[y, x])
#         plt.text(x, y, info,
#                  verticalalignment='center',
#                  horizontalalignment='center',
#                  color="white" if info > thresh else "black",fontsize=14)
#
#
# plt.subplot(1,2,2)
# matrix1 = [[70,3,0,2], [1,65,0,0],[1,1,74,0],[0,3,0,99]]
# matrix1 = np.array(matrix1)
# print(matrix1)
# plt.imshow(matrix1, cmap=plt.cm.Blues)
# plt.rcParams['font.sans-serif'] = 'Times New Roman'
# # plt.rcParams['figure.dpi'] = 600
# # 设置x轴坐标label
# plt.xticks(range(num_classes), labels, rotation=45,fontsize=14)
# # 设置y轴坐标label
# plt.yticks(range(num_classes), labels,fontsize=14)
# # 显示colorbar
# plt.colorbar(fraction=0.05, pad=0.05)
# plt.ylabel('True Labels',fontsize=14)
# plt.xlabel('Predicted Labels\n(b)',fontsize=14)
# plt.title('Confusion matrix',fontsize=14)
#
# # 在图中标注数量/概率信息
# thresh = matrix1.max() / 2
# for x in range(num_classes):
#     for y in range(num_classes):
#         # 注意这里的matrix[y, x]不是matrix[x, y]
#         info = int(matrix1[y, x])
#         plt.text(x, y, info,
#                  verticalalignment='center',
#                  horizontalalignment='center',
#                  color="white" if info > thresh else "black",fontsize=14)
#
# plt.tight_layout()
# plt.savefig("confusionmatrix.png",dpi=600)
# plt.show()


# plot delong test
# num_classes = 6
# labels = ['AlexNet','VGG-16','Inception-V3','ResNet34','ResNet50','ViT']
# matrix = [[ 0.36505,0.2966,0.1484,0.3657,0.4365], [3,36,0,5],[1,1,23,0],[0,0,0,30]]
# matrix = np.array(matrix)
# print(matrix)
# plt.imshow(matrix, cmap=plt.cm.Blues)

# # 设置x轴坐标label
# plt.xticks(range(num_classes), labels, rotation=45,fontsize=14)
# # 设置y轴坐标label
# plt.yticks(range(num_classes), labels,fontsize=14)
# # 显示colorbar
# plt.colorbar()
# # plt.xlabel('True Labels',fontsize=14)
# # plt.ylabel('Predicted Labels',fontsize=14)
# plt.title('P Value',fontsize=14)

# # 在图中标注数量/概率信息
# thresh = matrix.max() / 2
# for x in range(num_classes):
#     for y in range(num_classes):
#         # 注意这里的matrix[y, x]不是matrix[x, y]
#         info = int(matrix[y, x])
#         plt.text(x, y, info,
#                  verticalalignment='center',
#                  horizontalalignment='center',
#                  color="white" if info > thresh else "black",fontsize=14)
# plt.tight_layout()
# plt.show()
