import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('ToM.jpg')


def rescaleFrame(frame,scale=0.75):
  width=int(frame.shape[1]*scale)
  height=int(frame.shape[0]*scale)

  dimensions=(width,height)

  return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_image= rescaleFrame(img,scale=.1)
cv.imshow('image',resized_image)
# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(resized_image, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(resized_image, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

cv.waitKey(0)