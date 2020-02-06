import numpy as np 
import cv2 #opencv
x = cv2.imread('images.jpg')
print(x)
print(x.shape) (#total no. of matrix, total rows n columns)
#showing image
cv2.line(x,(0,0),(200,200),(0,0,255),5) #to draw line 2 coordinates of points 
cv2.imshow('fulldog',x) 
cv2.imshow('dog',x[0:200,100:400]) #crop image

cv2.waitKey(0) #for infinite time

