import cv2 
from imutils.video import VideoStream
import datetime
import imutils
import time
import argparse
import pyrealsense2 as rs
import numpy as np
import argparse

pipeline=rs.pipeline()
pipeline.start()



ap=argparse.ArgumentParser()
ap.add_argument("-v","--video",help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args=vars(ap.parse_args())

if args.get("video",None) is None:
	vs= VideoStream(src=1).start()
	time.sleep(2.0)
else:
	vs=cv2.VideoCapture(args["video"])

firstFrame=None

while True:
	#object "frame" configures the camera
	frame = pipeline.wait_for_frames()
	#frame=vs.read()
	color=frame.get_color_frame()
	frame = frame if args.get("video", None) is None else frame[1]
	text="Unoccupied"

	if frame is None:
		break

	#frame=imutils.resize(frame,width=500)
	#frame = imutils.resize(frame, width=500)
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	gray=cv2.GaussianBlur(gray,(21,21),0)

	if firstFram is None:
		firstFrame=gray
		continue

	frameDelta=cv2.absdiff(firstFrame,gray)
	thresh=cv2.threshold(frameDelta,25,25,cv2.THRESH_BINARY)[1]

	thresh =cv2.dilate(thresh,None,iterations=2)
	cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts=imutils.grab_contours(cnts)

	for c in cnts:
		if cv2.contourArea(c)<arg["min_area"]:
			continue

		(x,y,w,h)=cv2.boundingRect(c)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
		text="Occupied"

	cv2.putText(frame,"Room Status:{}".format(text),(10,20),
		cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
	cv2.imshow("security feed",frame)
	cv2.imshow("Thresh",thresh)
	cv2.imshw("Frame Delta",frameDelta)
	key=cv2.waitKey(1) & 0xFF

	if key==ord("q"):
		break

   
pipeline.stop()
cv2.destroyAllWindows()





