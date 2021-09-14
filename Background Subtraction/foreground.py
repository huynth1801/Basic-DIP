import cv2
import numpy as np
import matplotlib.pyplot as plt

def resize(dst, img):
    width = img.shape[1]
    height = img.shape[0]

    dim = (width, height)
    resized = cv2.resize(src=dst, dsize=dim, interpolation = cv2.INTER_AREA)
    return resized

def background_subtraction(foreground, background):
    foreground = np.copy(foreground)
    foreground = resize(foreground, background)
    # làm mờ ảnh foreground bằng bộ lọc làm mờ Gaussian
    foreground = cv2.GaussianBlur(foreground, (5,5), 0)

    diffence = cv2.absdiff(foreground,background)
    diffence = np.sum(diffence, axis=2) / 3.0
    _, diffence = cv2.threshold(diffence, 25, 255, cv2.THRESH_BINARY)
    #cv2.imshow("Foreground", diffence)
    #cv2.imwrite("foreground.png", diffence)
    #cv2.waitKey(0)
    return diffence
    




fg = cv2.imread('Image/pg4.png')
bg = cv2.imread('Image/background4.png')

foreground = background_subtraction(fg, bg)
plt.imshow(foreground, cmap='gray')
plt.axis('off')
plt.show()