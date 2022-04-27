
import matplotlib.pyplot as plt
from itertools import cycle
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc
from sklearn.utils.multiclass import type_of_target

# 加载数据
import glob
def roc_plot(label_list,score_list):
# Plot all ROC curves
    print(type_of_target(label_list))
    print(type_of_target(score_list))
    score_array = np.array(score_list)
    label_list = np.array(label_list)

#     y_label = label_binarize(label_list, classes=[0,1,2,3])
    fpr = []
    tpr = []
    roc_auc = []
    # for i in range(4):
    #     fpr[i], tpr[i], _ = roc_curve(y_label[:, i], score_array[:, i])
    #     roc_auc[i] = auc(fpr[i], tpr[i])
    fpr, tpr, _ = roc_curve(label_list, score_list)
    roc_auc = auc(fpr, tpr)
    return fpr,tpr,roc_auc
if __name__ == '__main__':
    data0 = pd.read_csv('./withoutpretraining/ResultalexnetFalse.csv')
    label_0,score_0 = data0.label.values,data0.score.values
    data1 = pd.read_csv('./withoutpretraining/Resultvgg16False.csv')
    label_1,score_1 = data1.label.values,data1.score.values
    data2 = pd.read_csv('./withoutpretraining/Resultinception_v3False.csv')
    label_2,score_2 = data2.label.values,data2.score.values
    data3 = pd.read_csv('./withoutpretraining/Resultresnet34False.csv')
    label_3,score_3 = data3.label.values,data3.score.values
    data4 = pd.read_csv('./withoutpretraining/Resultresnet50False.csv')
    label_4,score_4 = data4.label.values,data4.score.values
    data5 = pd.read_csv('./withoutpretraining/ResultViT.csv')
    label_5,score_5 = data5.label.values,data5.score.values
    data6 = pd.read_csv('./withoutpretraining/Resultmobilenet_v2False.csv')
    label_6,score_6 = data6.label.values,data6.score.values
    fpr_0, tpr_0, roc_auc_0 = roc_plot(label_0, score_0)
    fpr_1, tpr_1, roc_auc_1 = roc_plot(label_1, score_1)
    fpr_2, tpr_2, roc_auc_2 = roc_plot(label_2, score_2)
    fpr_3, tpr_3, roc_auc_3 = roc_plot(label_3, score_3)
    fpr_4, tpr_4, roc_auc_4 = roc_plot(label_4, score_4)
    fpr_5, tpr_5, roc_auc_5 = roc_plot(label_5, score_5)
    fpr_6, tpr_6, roc_auc_6 = roc_plot(label_6, score_6)

lw=2
plt.figure()
plt.plot(fpr_0, tpr_0,
         label='ROC curve of AlexNet (area = {:.2f})'.format(roc_auc_0),
         color='deeppink', linestyle='-', linewidth=2)
plt.plot(fpr_1, tpr_1,
         label='ROC curve of VGG-16 (area = {:.2f})'.format(roc_auc_1),
         color='aqua', linestyle='-', linewidth=2)
plt.plot(fpr_2, tpr_2,
         label='ROC curve of Inception-V3 (area = {:.2f})'.format(roc_auc_2),
         color='darkorange', linestyle='-', linewidth=2)
plt.plot(fpr_3, tpr_3,
         label='ROC curve of ResNet34 (area = {:.2f})'.format(roc_auc_3),
         color='cornflowerblue', linestyle='-', linewidth=2)
plt.plot(fpr_4, tpr_4,
         label='ROC curve of ResNet50 (area = {:.2f})'.format(roc_auc_4),
         color='coral', linestyle='-', linewidth=2)
plt.plot(fpr_5, tpr_5,
         label='ROC curve of ViT (area = {:.2f})'.format(roc_auc_5),
         color='navy', linestyle='-', linewidth=2)
plt.plot(fpr_6, tpr_6,
         label='ROC curve of MobileNet-V2 (area = {:.2f})'.format(roc_auc_6),
         color='chocolate', linestyle='-', linewidth=2)
# plt.plot(fpr["macro"], tpr["macro"],
#          label='macro-average ROC curve (area = {0:0.2f})'
#                ''.format(roc_auc["macro"]),
#          color='navy', linestyle=':', linewidth=4)

# colors = cycle(['aqua', 'darkorange', 'cornflowerblue'])
# for i, color in zip(range(n_classes), colors):
#     plt.plot(fpr[i], tpr[i], color=color, lw=lw,
#              label='ROC curve of class {0} (area = {1:0.2f})'
#              ''.format(i, roc_auc[i]))

plt.plot([0, 1], [0, 1], 'k--', lw=lw)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('The ROC curves of different models with pre-trained')
plt.legend(loc="lower right")
plt.show()
