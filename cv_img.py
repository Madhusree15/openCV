import cv2 as cv

#image
'''img=cv.imread("cat.jpg")
cv.imshow('cat',img)
cv.waitKey(0)'''


#video
'''capture=cv.VideoCapture('dog.mp4')
while True:
    isTrue,frame=capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xff==ord('d'):
        break
capture.release()
cv.destroyAllWindows()'''

#resize the video

'''def rescaleFrame(frame,scale=0.75):
  width=int(frame.shape[1]*scale)
  height=int(frame.shape[0]*scale)

  dimensions=(width,height)

  return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

capture=cv.VideoCapture('dog.mp4')

while True:

    isTrue,frame=capture.read()

    frame_Resized=rescaleFrame(frame,scale=.2)
    cv.imshow('video',frame)
    cv.imshow('video Resized',frame_Resized)

    if cv.waitKey(20) & 0xff==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
'''

#resizing the photo
'''img=cv.imread("cat.jpg")
cv.imshow('cat',img)
def rescaleFrame(frame,scale=0.75):
  width=int(frame.shape[1]*scale)
  height=int(frame.shape[0]*scale)

  dimensions=(width,height)

  return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_image= rescaleFrame(img,scale=.1)
cv.imshow('image',resized_image)
cv.waitKey(0)'''

#for live videos use the below function instead of rescaleframe to change resolution
'''def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)'''


