clc;
clear;
close all;

fuse_matrix=rand(5)%产生矩阵

imagesc(fuse_matrix)
set(gca,'xtick',1:4)
set(gca,'xticklabel',{'CLE','PLE','PSE','NLP'},'XTickLabelRotation',45)%设置横轴和横轴标签大小
set(gca,'ytick',1:4)
set(gca,'yticklabel',{'CLE','PLE','PSE','NLP'})%设置纵轴
set(gca,'FontSize',14,'Fontname', 'Times New Roman');%设置坐标系的数字大小
colorbar