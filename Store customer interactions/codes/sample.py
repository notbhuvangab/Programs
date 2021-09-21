import cv2
import time
cap=cv2.VideoCapture('Part1.mp4')
ptime=0
while True:
  sucess,img=cap.read()
  ctime=time.time()
  fps=1/(ctime-ptime)
  ptime=ctime

  cv2.putText(img, str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN ,3,(255,0,0),3)

  cv2.imshow('image',img)

  cv2.waitKey(10)