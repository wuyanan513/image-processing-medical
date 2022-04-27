from PIL import Image,ImageOps
import numpy as np
from tqdm import trange
import os
import matplotlib.pyplot as plt
from skimage import transform
if __name__ == '__main__':
    patient_num = 102
    all_img_path = r'G:\3-airway-and-lungfield-paper\5-snapshots\lungmask\nnunet_method\HC\dalian'
    save_path = r'G:\3-airway-and-lungfield-paper\5-snapshots\lungmask\npy\nnunet\dalian\HC'
    for i in trange(1,patient_num):
        img_path = os.path.join(all_img_path,str(i))
        img_list = os.listdir(img_path)
        new_img_data = []
        for k in range(len(img_list)):
            if not img_list[k].endswith('png'):  # 若不是png文件，跳过
                continue
            img_all = os.path.join(img_path, img_list[k])
            img_data = Image.open(img_all).convert('L')
            # getbbox实际上检测的是黑边，所以要先将image对象反色
            ivt_image = ImageOps.invert(img_data)
            padding = (0, 0, 0, 0)
            # 如果担心检测出来的bbox过小，可以加点padding
            bbox = ivt_image.getbbox()
            left = bbox[0] - padding[0]
            top = bbox[1] - padding[1]
            right = bbox[2] + padding[2]
            bottom = bbox[3] + padding[3]
            cropped_image = img_data.crop([left, top, right, bottom])
            new_img = np.array(cropped_image)
            # plt.imshow(new_img, 'gray')
            # plt.show()
            new_img = transform.resize(new_img, [224, 224])
            new_img_data.append(new_img)
        new_img_data = np.array(new_img_data)
        save_img_path = os.path.join(save_path,str(i))
        save_img_path = save_img_path+'.npy'
        np.save(save_img_path, new_img_data)

