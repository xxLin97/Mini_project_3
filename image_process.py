
import cv2 as cv
import numpy as np

def blur_demo(image):      
    dst = cv.blur(image, (1, 15))   
    cv.namedWindow('blur_demo', cv.WINDOW_NORMAL)
    cv.imshow("blur_demo", dst)

def median_blur_demo(image):    
    dst = cv.medianBlur(image, 5)
    cv.namedWindow('median_blur_demo', cv.WINDOW_NORMAL)
    cv.imshow("median_blur_demo", dst)

def custom_blur_demo(image):    
    kernel = np.ones([5, 5], np.float32)/25   
    dst = cv.filter2D(image, -1, kernel)
    cv.namedWindow('custom_blur_demo', cv.WINDOW_NORMAL)
    cv.imshow("custom_blur_demo", dst)

src = cv.imread('C:\Desktop\lena.jpg')
cv.namedWindow('input_image', cv.WINDOW_NORMAL)
cv.imshow('input_image', src)

blur_demo(src)
median_blur_demo(src)
custom_blur_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()