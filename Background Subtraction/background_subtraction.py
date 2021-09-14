from typing import DefaultDict
import cv2
import numpy as np
import matplotlib.pyplot as plt

def resize(dst, img):
    width = img.shape[1]
    height = img.shape[0]

    dim = (width, height)
    resized = cv2.resize(src=dst, dsize=dim, interpolation = cv2.INTER_AREA)
    return resized



def background_subtraction(fg_img, bg_img, weather_bg):
    fg_img = cv2.GaussianBlur(fg_img, (5, 5), 0)

    
    diff1 = cv2.subtract(fg_img,bg_img)
    diff2 = cv2.subtract(bg_img,fg_img)
    diff = diff1+diff2
    diff[abs(diff)<13.0]=0
    gray = cv2.cvtColor(diff.astype(np.uint8), cv2.COLOR_BGR2GRAY)
    gray[np.abs(gray) < 10] = 0
    fgmask = gray.astype(np.uint8)
    fgmask[fgmask>0]=255

    #invert the mask
    fgmask_inv = cv2.bitwise_not(fgmask)
    #use the masks to extract the relevant parts from FG and BG
    fgimg = cv2.bitwise_and(fg_img,fg_img,mask = fgmask)
    bgimg = cv2.bitwise_and(bg_img,bg_img,mask = fgmask_inv)
    weather_img = cv2.bitwise_and(weather_bg,weather_bg,mask = fgmask_inv)

    cv2.imshow('MC image', fg_img)
    cv2.imshow('Background image', bg_img)
    cv2.imshow('Segmented image', fgimg)
    cv2.imshow('Mask', fgmask)
    cv2.waitKey(0)
    return fgimg, weather_img



bg1 = cv2.imread('Image/background4.png')
#print(bg1.shape)
pg4 = cv2.imread('Image/pg4.png')
#print(pg4.shape)
weather = cv2.imread('Image/weather_forecast.jpg')
weather_re = resize(weather, bg1)

weather_re = resize(weather, bg1)
fgimg, weather_forecast = background_subtraction(pg4, bg1, weather_re)
#combine both the BG and the FG images
dst = cv2.add(weather_forecast, fgimg)
cv2.imshow('Background Removal',dst)
cv2.imwrite('Background_Removal.png',dst)
cv2.waitKey(0)