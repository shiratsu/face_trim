# -*- coding: utf-8 -*-

import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys, os
from PIL import Image
import os
# %matplotlib inline

#os.mkdir('./image/faces/sugar')
#os.mkdir('./image/faces/salt/takeuchi_ryoma')

#入力ファイルのパスを指定
in_jpg = "./"+sys.argv[1]+"/"
out_jpg = "./"+sys.argv[1]+"/"+sys.argv[2]+"/"

#リストで結果を返す関数
def get_file(dir_path):
    filenames = os.listdir(dir_path)
    return filenames

pic = get_file(in_jpg)

for i in pic:
    # 画像の読み込み
    image_gs = cv2.imread(in_jpg + i)

    # 顔認識用特徴量ファイルを読み込む --- （カスケードファイルのパスを指定）
    cascade = cv2.CascadeClassifier("/usr/local/opt/opencv/share/OpenCV/haarcascades/"+sys.argv[3])

    # 顔認識の実行
    face_list = cascade.detectMultiScale(image_gs,scaleFactor=1.1,minNeighbors=1,minSize=(1,1))

    # 顔だけ切り出して保存
    no = 1;
    for rect in face_list:
        x = rect[0]
        y = rect[1]
        width = rect[2]
        height = rect[3]
        dst = image_gs[y:y + height, x:x + width]
        save_path = out_jpg + '/' + str(i)

        #認識結果の保存
        a = cv2.imwrite(save_path, dst)
        # plt.show(plt.imshow(np.asarray(Image.open(save_path))))
        # print(no)
        no = no + 1
