import SimpleITK as sitk
import os
import numpy as np
from PIL import Image
import xlrd
import matplotlib.pyplot as plt
import collections
import xlwt


def xls_read(xls_path):
    folder_name=[]
    upper=[]
    middle=[]
    lower=[]
    read_book=xlrd.open_workbook(xls_path)
    table=read_book.sheet_by_index(0)
    nrows=table.nrows
    # read value and save
    for i in range(1,nrows):
        folder_name.append(int(table.cell_value(i,0)))
        upper.append(int(table.cell_value(i,1)))
        middle.append(int(table.cell_value(i,2)))
        lower.append(int(table.cell_value(i,3)))
    return  folder_name,upper,middle,lower
        
def localization(img,mask,upper,middle,lower):
    upper_img = []
    middle_img = []
    lower_img = []
    upper_img_new=[]
    middle_img_new=[]
    lower_img_new=[]
    # read dicom series
    reader = sitk.ImageSeriesReader()
    img_names = reader.GetGDCMSeriesFileNames(img)
    reader.SetFileNames(img_names)
    img_sitk = reader.Execute()
    img_arr = sitk.GetArrayFromImage(img_sitk)
    len_arr = len(img_arr)
    

    # read lung mask
    mask_sitk_img = sitk.ReadImage(mask)
    mask_arr = sitk.GetArrayFromImage(mask_sitk_img)
    mask_arr[mask_arr>0]=1
    # read the slices of upper, middle, and lower
    ST = img_sitk.GetSpacing()[2]
    index_upper,index_middle,index_lower = len_arr-upper,len_arr-middle,len_arr-lower  # 找被标注的层

    upper_img = img_arr[index_upper:int(index_upper+10/ST),:,:]
    middle_img = img_arr[index_middle:int(index_middle+10/ST), :, :] 
    lower_img = img_arr[int(index_lower-30/ST):index_lower, :, :]

    # The value limited in lung field
    upper_mask = mask_arr[index_upper:int(index_upper+10/ST), :, :]
    middle_mask = mask_arr[index_middle:int(index_middle+10/ST), :, :] 
    lower_mask = mask_arr[int(index_lower-30/ST):index_lower, :, :]
    
    
    upper_img[upper_mask != 1] = -1024
    middle_img[middle_mask != 1] = -1024
    lower_img[lower_mask != 1] = -1024

    upper_ratio = calculate_em(upper_img,upper_mask)
    middle_ratio = calculate_em(middle_img,middle_mask)
    lower_ratio = calculate_em(lower_img,lower_mask)
    return upper_ratio,middle_ratio,lower_ratio
    # MIN_BOUND = -1000.0
    # MAX_BOUND = 400.0
    # img_arr[img_arr > MAX_BOUND] = MAX_BOUND
    # img_arr[img_arr < MIN_BOUND] = MIN_BOUND
    # img_arr = (img_arr - MIN_BOUND) / (MAX_BOUND - MIN_BOUND) * 255
    # new_img_arry = img_arr[index, :, :]
    # new_mask_arry = mask_arr[index, :, :]
def calculate_em(img,mask):
    # calculate the number of <-950 HU
    save_arr = np.zeros_like(img)
    temp = np.zeros_like(img)
    temp[img > -1024] += 1
    temp[img < -950] += 1
    save_arr[temp == 2] = 2
    lobe_count1 = collections.Counter(save_arr.flatten())
    em_count = lobe_count1[2]

    # calculate the number of lung
    lobe_count2 = collections.Counter(mask.flatten())
    lung_count = lobe_count2[1]

    ratio_em = em_count/lung_count*100
    ratio_em = round(ratio_em,2)
    # print (ratio_em)
    return ratio_em

def visualization(img):
    img_len = len(img)
    for i in range(img_len):
        plt.subplot(2,int(img_len/2),i+1)
        plt.imshow(img[i,:,:],'gray')
        plt.axis('off')
    # plt.tight_layout()
    # plt.savefig(str(name)+'.jpg',
    #         dpi=400,bbox_inches = 'tight')
    plt.show()
    # color_map = get_color_map_list(5)  # 设置color_map 方便查看
    # color_map[0]=0
    # mask_pil = Image.fromarray(img.astype(np.uint8), mode='P')
    # mask_pil.putpalette(color_map)


if __name__ == '__main__':
    mask_path=os.listdir('I:\data\data2slung')
    # print(mask_path[0])
    xls_path='I:/data/localization1.xlsx'
    folder_name,upper,middle,lower = xls_read(xls_path)
    upper_ratio_all=[]
    middle_ratio_all=[]
    lower_ratio_all=[]
    name = []
    for i in range(len(upper)):#len(folder_name)+1
        img_path = 'I:/data/data2s/'+str(folder_name[i])
        lung_mask_path = os.path.join('I:\data\data2slung', mask_path[i])
        upper_ratio,middle_ratio,lower_ratio = localization(img_path,lung_mask_path,upper[i],middle[i],lower[i])
        upper_ratio_all.append(upper_ratio)
        middle_ratio_all.append(middle_ratio)
        lower_ratio_all.append(lower_ratio)
        name.append(str(folder_name[i]))
        # visualization(upper_img)
        # visualization(middle_img) 
        # visualization(lower_img)len(upper_ratio_all)
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)
    for i in range(len(upper_ratio_all)):
        sheet.write(i, 0, name[i])
        sheet.write(i, 1, upper_ratio_all[i])
        sheet.write(i, 2, middle_ratio_all[i])
        sheet.write(i, 3, lower_ratio_all[i])
        # sheet.write(i, 0, f_path[i])
        # sheet.write(i, 1, ctpath[i])
    book.save('./ratio2.xls')    
