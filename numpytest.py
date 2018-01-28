# -*- coding: utf-8 -*-
import numpy as np

def main():

    # 2次元配列の宣言・初期化
    A = np.array([[1, 2],
                  [3, 4],
                  [5, 6]])
    A = np.array([1,2])

    # 行列の大きさ
    print("行列Aの大きさ:", A.shape)
    print("行列Aの行数:", A.shape[0])
    print("行列Aの列数:", A.shape[1])


if __name__ == '__main__':
    main()
