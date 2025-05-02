import cv2 as cv
import numpy as np

img = cv.imread('cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

square= cv.rectangle(blank, (img.shape[1]//2 ,img.shape[0]//2), (img.shape[1]//2 + 100,img.shape[0]//2+100), 255, -1)
cv.imshow('square',square)

weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Weird Shaped Masked Image', masked)

masks = cv.bitwise_and(img,img,mask=square)
cv.imshow('square Shaped Masked Image', masks)

cv.waitKey(0)