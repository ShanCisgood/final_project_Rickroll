import cv2
import os
import math
from capture_frame import capture_frames
from target_preprocess import resize_the_target_img

# 用 dict 儲存每一張圖的直方圖
def build_idx() -> dict:
    read_path = 'frame_data'
    files = os.listdir(read_path)
    dist = {}

    for f in files:
        img_path = read_path + '/' + f
        img = cv2.imread(img_path)
        hist = []

        for i in range(3):
            ht = cv2.calcHist([img], [i], None, [256], [0, 256])
            hist.append(ht)
        dist[f] = hist
    
    return dist

# 把東西都替換成 Rick
def match_replace(dist, h, w):
    image = cv2.imread('target_data/target.jpg')

    for i in range(0, h, 48):
        for j in range(0, w, 64):
            img = image[i: i + 48, j: j + 64, 0: 3]

            hist = []
            for k in range(3):
                ht = cv2.calcHist([img], [k], None, [256], [0, 256])
                hist.append(ht)

            sim = 0.0
            for key in dist: # 比較 RGB 的直方圖
                match0 = cv2.compareHist(hist[0], dist[key][0], cv2.HISTCMP_CORREL)
                match1 = cv2.compareHist(hist[1], dist[key][1], cv2.HISTCMP_CORREL)
                match2 = cv2.compareHist(hist[2], dist[key][2], cv2.HISTCMP_CORREL)
                match = match0 + match1 + match2

                if match > sim:
                    sim = match
                    rename = key
            if i + 48 <= h and j + 64 <= w: # 大小塞得下才替換
                image[i: i + 48, j : j + 64, 0: 3] = cv2.imread('frame_data/' + rename)
        cv2.imwrite('finish_img3.jpg', image)
    print('replacing done.')

if __name__ == '__main__':
    capture_frames()
    w, h = resize_the_target_img()
    dist = build_idx()
    match_replace(dist, w, h)