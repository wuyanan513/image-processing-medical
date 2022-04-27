import SimpleITK as sitk
import os
import numpy as np
import tqdm
import copy
import cv2

def get_ct_file(main_path):
    ctpath = []
    # 遍历该文件夹下的所有目录或者文件
    for root, s_dirs, _ in os.walk(main_path, topdown=True):  # 获取 train文件下各文件夹名称
        for sub_dir in s_dirs:
            i_dir = os.path.join(root, sub_dir) # 获取各类的文件夹 绝对路径
            img_list = os.listdir(i_dir)                    # 获取类别文件夹下所有png图片的路径
            for i in range(len(img_list)):
                if img_list[i].endswith('.gz'):
                    path = os.path.join(i_dir, img_list[i])
                    ctpath.append(path)
    return ctpath

def erode(new_img_arr):
    shape = new_img_arr.shape
    erode_img_arr = np.zeros(shape)
    for i in range(shape[0]):
        kernel = np.ones((3, 3), np.uint8)
        erode_img_arr[i, :, :] = cv2.erode(new_img_arr[i, :, :], kernel, iterations=5)
    return erode_img_arr


# def get_listdir(path):
#     tmp_list = []
#     for file in os.listdir(path):
#         if os.path.splitext(file)[1] == '.gz':
#             file_path = os.path.join(path, file)
#             tmp_list.append(file_path)
#     return tmp_list


def crop(img_path, lobe_mask_path, img_save_path):
    img_sitk = sitk.ReadImage(img_path)
    img_arr = sitk.GetArrayFromImage(img_sitk)
    lobe_mask_sitk = sitk.ReadImage(lobe_mask_path)
    lobe_mask_arr = sitk.GetArrayFromImage(lobe_mask_sitk)
    lobe_mask_arr[lobe_mask_arr != 0] = 1
    lobe_mask_arr = erode(lobe_mask_arr)

    img_arr[lobe_mask_arr != 1] = -1000

    print(img_arr.shape, end=" ")

    sums = np.sum(np.sum(lobe_mask_arr, axis=1), axis=1)

    # Track all =0 layers from front from that axis
    remove_front_index = 0
    while sums[remove_front_index] == 0:
        remove_front_index += 1

    # Track all =0 layers from back from that axis
    remove_back_index = len(sums) - 1
    while sums[remove_back_index] == 0:
        remove_back_index -= 1

    # Remove those layers
    img_arr = np.delete(
        img_arr, list(range(remove_front_index - 1)) + list(range(remove_back_index + 2, len(sums))),
        axis=0
    )

    lobe_mask_arr = np.delete(
        lobe_mask_arr, list(range(remove_front_index - 1)) + list(range(remove_back_index + 2, len(sums))),
        axis=0
    )

    print(" -> ", img_arr.shape, end=" ")

    new_img = sitk.GetImageFromArray(img_arr)
    new_img.SetDirection(img_sitk.GetDirection())
    new_img.SetOrigin(img_sitk.GetOrigin())
    new_img.SetSpacing(img_sitk.GetSpacing())
    _, fullflname = os.path.split(img_path)
    sitk.WriteImage(new_img, img_path.replace('image','lung_data'))
    #
    # new_lobe = sitk.GetImageFromArray(lobe_mask_arr)
    # new_lobe.SetDirection(img_sitk.GetDirection())
    # new_lobe.SetOrigin(img_sitk.GetOrigin())
    # new_lobe.SetSpacing(img_sitk.GetSpacing())
    # _, fullflname = os.path.split(img_path)
    # sitk.WriteImage(new_lobe, os.path.join(lung_mask_save_path, fullflname))


if __name__ == '__main__':
    img_path = r'E:\1-paper\4-GOLD\data\image'

    lung_mask_path = r'E:\1-paper\4-GOLD\data\lung_mask'
    img_save_path = r'E:\1-paper\3-MIP-classification\data\lung_image'
    # lung_mask_save_path = r'I:\paper\1-images\COPD\dalian_before\lungmask'

    img = get_ct_file(img_path)
    img.sort()
    l_mask = get_ct_file(lung_mask_path)
    l_mask.sort()
    for i in tqdm.trange(len(img)):
        crop(img[i], l_mask[i], img_save_path)