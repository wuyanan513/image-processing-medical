import sys
from glob import glob
from PIL import Image
%matplotlib inline
from matplotlib import pyplot as plt
import os
import cv2
import json
import pandas as pd
import numpy as np
from glob import glob 
from tqdm import tqdm
from IPython import embed
import base64
import csv
from tqdm import trange
import xml.etree.cElementTree as ET
# from labelme import utils

if sys.version_info[0] == 2:
    import xml.etree.cElementTree as ET
else:
    import xml.etree.ElementTree as ET

font = cv2.FONT_HERSHEY_SIMPLEX

color_mode = [(0,0,255),(0,255,0),(255,0,0),(0,255,255),(255,0,255),(255,255,0),(255,255,255)]

plt.figure(figsize=(10, 10))

image_path = r"G:\bleeding\labelled_images\blood_fresh\Blood - fresh"
csv_file = r"G:\bleeding\metadata.csv"
csvfile = open( r"G:\bleeding\metadata.csv",'r')
annotations = [each for each in csv.DictReader(csvfile, delimiter=';')]
# annotations = pd.read_csv(csv_file,header=None).values
# category = reader['finding_category']
img_name = os.listdir(image_path)
total_csv_annotations = []
total_position = []
for annotation in annotations:
    key = annotation['filename']#.split(os.sep)[-1]
    # name = annotation['filename']
    position = [annotation['x1'],annotation['y1'],annotation['x2'],annotation['y2'],annotation['x3'],
    annotation['y3'],annotation['x4'],annotation['y4']]
    name = key
    if key in img_name:
        pts = ['xmin', 'ymin', 'xmax', 'ymax']
        bndbox = [min(position[0],position[2],position[4],position[6]),min(position[1],position[3],position[5],position[7]),
                max(position[0],position[2],position[4],position[6]),max(position[1],position[3],position[5],position[7])]
        img = cv2.imread(os.path.join(image_path,key))
            
        top_corner, down_corner = (int(bndbox[0]), int(bndbox[1])), (int(bndbox[2]), int(bndbox[3]))
        cv2.rectangle(img, top_corner, down_corner, color_mode[0], thickness=2)
        # cv2.putText(img,str(name),(top_corner[0]+5, top_corner[1]+25), font, 1,color_mode[1],1,cv2.LINE_AA)       
        plt.imshow(img[:,:,::-1])
        plt.axis('off')
        plt.show()
