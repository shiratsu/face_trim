# -*- coding: utf-8 -*-
import sys
import os
import csv

if __name__ == '__main__':
  outdir = sys.argv[1]

  if not os.path.isdir(outdir):
    sys.exit('%s is not directory' % outdir)

  names = {
    "hiratsuka": 0,
    "sakuma": 1,
    "fujisaki": 2,
  }

  #exts = ['.PNG','.JPG','.JPEG']
  exts = ['.JPG','.JPEG','.PNG']

  with open('some.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    for dirpath, dirnames, filenames in os.walk(outdir):
        for dirname in dirnames:
            print(dirname)
            print("-------------------------")
            print(dirpath)
            print("-------------------------")
            if dirname in names:
                n = names[dirname]
                member_dir = os.path.join(dirpath, dirname)
                print(member_dir)
                print("-------------------------")
                for dirpath2, dirnames2, filenames2 in os.walk(member_dir):
                    if not dirpath2.endswith(dirname):
                        continue
                    for filename2 in filenames2:
                        (fn,ext) = os.path.splitext(filename2)
                        if ext.upper() in exts:
                            img_path = os.path.join(dirpath2, filename2)
                            print(img_path)
                            print("-------------------------")
                            csv_array = [img_path,n]
                            writer.writerow(csv_array)     # list（1次元配列）の場合
