import pandas as pd


def get_listdir(path):  # 获取目录下所有gz格式文件的地址，返回地址list
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    return tmp_list

if __name__ == '__main__':
    if __name__ == '__main__':
        img_path = r'C:\Users\user\Desktop\temp\nii'
        mask_path = r'C:\Users\user\Desktop\temp\mask'
        save_path = r'C:\Users\user\Desktop\temp\nii_lung'
        img_list = get_listdir(img_path)
        img_list.sort()