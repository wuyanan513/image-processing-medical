import matplotlib.pyplot as plt
import albumentations as A
from pycocotools.coco import COCO
import skimage.io as io

an_train_file = '/media/data10/zl/cv/11公开数据集/coco2017/annotations_trainval2017/annotations/instances_val2017.json'
coco = COCO(an_train_file)
# 加载并显示指定id的图片
# get all images containing given categories, select one at random
catIds = coco.getCatIds(catNms=['dog'])
imgIds = coco.getImgIds(catIds=catIds)
I = coco.loadImgs(imgIds[2])[0]
img = io.imread(I['coco_url'])
# tranform pipline
transform = A.Compose([A.RandomCrop(width=256,height=256),
                       A.HorizontalFlip(p=0.5),
                       A.RandomBrightnessContrast(p=0.2)])
# 图像喂入pipeline
transformed = transform(image=img)
transformed_image = transformed['image']
plt.figure(figsize=(20,20))
plt.subplot(1,2,1)
plt.axis('off')
plt.title('org img')
plt.imshow(img)
plt.subplot(1,2,2)
plt.imshow(transformed_image)
plt.axis('off')
plt.title('transformed image')
plt.show()

# mask augmentation
import matplotlib.pyplot as plt
import albumentations as A
from pycocotools.coco import COCO
import skimage.io as io
import cv2
import numpy as np

an_train_file = '/media/data10/zl/cv/11公开数据集/coco2017/annotations_trainval2017/annotations/instances_val2017.json'
coco = COCO(an_train_file)
# 加载并显示指定id的图片
# get all images containing given categories, select one at random
catIds = coco.getCatIds(catNms=['person','dog'])
imgIds = coco.getImgIds(catIds=catIds)
imgId = imgIds[0]
annIds = coco.getAnnIds(imgIds=imgId,catIds=catIds)
anns = coco.loadAnns(annIds)
I = coco.loadImgs(imgId)[0]
img = io.imread(I['coco_url'])
# 显示原始图片
plt.figure(figsize=(20,20))
plt.subplot(2,2,1)
plt.imshow(img)
plt.axis('off')
plt.title('org image')
plt.subplot(2,2,2)
#获取原始分割图像,cv2手工画mask
mask1 = np.zeros(img.shape,dtype=np.uint8)
for ann1 in anns:
    # 获取category
    category1 = ann1['category_id']*10
    color1 = (category1,category1,category1)
    box1 = ann1['bbox']
    x1,y1,width1,height1 = [int(i) for i in box1]
    color2 = [np.random.randint(0,255) for i in range(3)]
    # 坐标
    for seg in ann1['segmentation']:
        poly = np.array(seg).reshape((int(len(seg) / 2), 2)).astype(np.int32)
        box = poly.reshape((-1,1,2))
        # 填充
        cv2.fillPoly(mask1,[poly],color1)
plt.imshow(mask1)
plt.axis('off')
plt.title('org mask')
# 增强pipeline
transform = A.Compose([A.RandomCrop(width=256,height=256),
                       A.HorizontalFlip(p=0.5),
                       A.RandomBrightnessContrast(p=0.2)])

# 图像喂入pipeline
transformed = transform(image=img,mask=mask1)
transformed_image = transformed['image']
transform_mask = transformed['mask']
plt.subplot(2,2,3)
plt.imshow(transformed_image)
plt.axis('off')
plt.title('transformed image')
plt.subplot(2,2,4)
plt.axis('off')
plt.imshow(transform_mask)
plt.title('tranformed mask')
plt.show()
