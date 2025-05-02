import cv2 as cv
import numpy as np

#to display balnk picture
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow("Blank",blank)

#1.paint the image a certain colour
#blank[200:300,300:400]=0,0,255
#cv.imshow('Red',blank)

#2.draw a reactagle
'''cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=cv.FILLED)#instead of cv.filled replace with -1
cv.imshow('rectangle',blank)'''

#3.CIRCLE
'''cv.circle(blank,(250,250),40,(0,0,255),thickness=3)
cv.imshow('circle',blank)'''

#line
'''cv.line(blank,(0,0),(250,250),(255,255,255),thickness=3)
cv.imshow('Line',blank)'''

#write text
cv.putText(blank,'Hello my name is madhu',(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),3)
cv.imshow('Text',blank)

#img=cv.imread("cat1.jpg")
#cv.imshow('cat',img)
cv.waitKey(0)