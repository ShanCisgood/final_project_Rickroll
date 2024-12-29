import cv2
import os
import math

def resize_the_target_img():
    img = cv2.imread("raw_data/yes_why.jpg")
    # print(img.shape)
    w, h, ch = img.shape
    gcd_w = math.gcd(w, 64)
    gcd_h = math.gcd(h, 48)
    scale = math.gcd(gcd_w, gcd_h)
    if scale == 1:
        scale *= 32
    while scale * h > 8192 or scale * w > 8192:
        scale -= 1
    img = cv2.resize(img, (h * scale, w * scale))

    try: 
        if not os.path.exists('target_data'): 
            os.makedirs('target_data') 
    
    except OSError: 
        print ('Error: Creating directory of data')

    cv2.imwrite('./target_data/target.jpg', img)

    return w * scale, h * scale