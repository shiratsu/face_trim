# -*- coding: utf-8 -*-

import csv
import numpy as np
from PIL import Image, ImageTk
from keras.preprocessing.image import array_to_img, img_to_array, list_pictures, load_img


def main():
    (X_train, Y_train) = read_data('../deeplearning/train.txt')
    (imgs_test, labels_test) = read_data('../deeplearning/test.txt')
    print(X_train.shape)
    print(Y_train.shape)

def read_data(path):
    imgs = []
    labels = []
    f = open(path, 'r')
    dataReader = csv.reader(f)
    for row in dataReader:
        path = row[0]
        #img = Image.open(path, 'r')
        #img = np.asarray(img)
        img = img_to_array(load_img(path, target_size=(32,32)))
        imgs.append(img)
        label = row[1]
        labels.append(label)
        print("----------")
        print(img.shape)
        print(path)
    return (np.array(imgs), np.array(labels).reshape(-1,1))
