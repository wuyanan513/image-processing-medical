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
