from lungmask import mask  #lungmask refer:https://github.com/JoHof/lungmask
import SimpleITK as sitk
import os
from tqdm import trange
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
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
if __name__ == '__main__':
    main_path = r'H:\yxy_GOLD\image'
    # save_path = r'I:\mip_paper\2_lung_mask\HC'
    img_path = get_ct_file(main_path)
    img_path.sort()
    for i in trange(len(img_path)):
        input_path=os.path.join(main_path,img_path[i])
        input_image = sitk.ReadImage(input_path)
        segmentation = mask.apply(input_image) 
        new_mask_img1 = sitk.GetImageFromArray(segmentation)
        new_mask_img1.SetDirection(input_image.GetDirection())
        new_mask_img1.SetOrigin(input_image.GetOrigin())
        new_mask_img1.SetSpacing(input_image.GetSpacing())
        # new_file_path = save_path
        # path = os.path.join(new_file_path, img)
        path = input_path.replace('image','lung_mask')
        sitk.WriteImage(new_mask_img1, path)
