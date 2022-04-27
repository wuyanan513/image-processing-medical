# import os
# import numpy as np
# import SimpleITK as sitk
# from tqdm import trange
#
# if __name__ == '__main__':
#     # 原始数据，不能有中文
#     main_path = r'D:\train_data\CT\airway\nii'
#     path_name = os.listdir(main_path)
#     save_path = r'D:\train_data\CT\airway\nii'
#
#     for i in trange(len(path_name)):
#
#         sitk_img = sitk.ReadImage(os.path.join(main_path,path_name[i]))
#         img_arr = sitk.GetArrayFromImage(sitk_img)
#         img_arr[img_arr>0] = 1
#         # img_arr[img_arr == 75] = 2
#         # img_arr[img_arr == 255] = 0
#
#         img_arr = sitk.GetImageFromArray(img_arr)
#         img_arr.SetDirection(sitk_img.GetDirection())
#         img_arr.SetOrigin(sitk_img.GetOrigin())
#         img_arr.SetSpacing(sitk_img.GetSpacing())
#         path = os.path.join(save_path, path_name[i])
#         sitk.WriteImage(img_arr, path)
import SimpleITK as sitk
import os
import copy
import tqdm


def get_listdir(path):  # 获取目录下所有png格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list


def add_label(img, mask, path):
    img_sitk_img = sitk.ReadImage(img)
    mask_sitk_img = sitk.ReadImage(mask)
    mask_img_arr = sitk.GetArrayFromImage(mask_sitk_img)

    new_mask_img = sitk.GetImageFromArray(mask_img_arr)
    new_mask_img.SetDirection(img_sitk_img.GetDirection())
    new_mask_img.SetOrigin(img_sitk_img.GetOrigin())
    new_mask_img.SetSpacing(img_sitk_img.GetSpacing())
    _, fullflname = os.path.split(mask)
    sitk.WriteImage(new_mask_img, os.path.join(path, fullflname))


# 修正3d slicer不能读取的mask
if __name__ == '__main__':
    img_path = r'D:\train_data\nii'
    mask_path = r'D:\train_data\airway_shui'
    save_path = r'D:\train_data\airway_shui'
    img = get_listdir(img_path)
    mask = get_listdir(mask_path)
    img.sort()
    mask.sort()
    for i in tqdm.trange(len(mask)):
        add_label(img[i], mask[i], save_path)
